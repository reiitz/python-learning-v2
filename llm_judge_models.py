import sqlite3
from datetime import datetime

class Prompt:
    def __init__(self, text, category=None):
        self.text = text
        self.category = category
        self.id = None

    def save(self, db_path='llm_judge.db'):
        """Save prompt to database and set the id"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO prompts (text, category)
            VALUES (?, ?)
        ''', (self.text, self.category))

        self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return self.id

class Response:
    def __init__(self, prompt_id, llm_provider, response_text):
        self.prompt_id = prompt_id
        self.llm_provider = llm_provider
        self.response_text = response_text
        self.id = None

    def save(self, db_path='llm_judge.db'):
        """Save response to database"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO responses (prompt_id, llm_provider, response_text)
            VALUES (?, ?, ?)
        ''', (self.prompt_id, self.llm_provider, self.response_text))

        self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return self.id

class Evaluation:
    def __init__(self, response_id, criteria, score, feedback=None):
        self.response_id = response_id
        self.criteria = criteria
        self.score = score
        self.feedback = feedback
        self.id = None

    def save(self, db_path='llm_judge.db'):
        """Save evaluation to database"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO evaluations (response_id, criteria, score, feedback)
            VALUES (?, ?, ?, ?)
        ''', (self.response_id, self.criteria, self.score, self.feedback))

        self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return self.id

class Judge:
    def __init__(self, criteria_list):
        """
        criteria_list: list of criteria to evaluate responses on
        Example: ["clarity", "accuracy", "helpfulness"]
        """
        self.criteria_list = criteria_list

    def evaluate_response(self, response_id, scores_dict, db_path='llm_judge.db'):
        """
        Evaluate a response on multiple criteria

        Args:
            response_id: ID of the response to evaluate
            scores_dict: dict mapping criteria to (score, feedback)
                Example: {"clarity": (8, "Clear but needs examples")}

        Returns:
            list of evaluation IDs
        """
        evaluation_ids = []

        for criteria in self.criteria_list:
            if criteria in scores_dict:
                score, feedback = scores_dict[criteria]

                evaluation = Evaluation(
                    response_id=response_id,
                    criteria=criteria,
                    score=score,
                    feedback=feedback
                )
                eval_id = evaluation.save(db_path)
                evaluation_ids.append(eval_id)

        return evaluation_ids

    def get_average_score(self, response_id, db_path='llm_judge.db'):
        """Calculate average score across all criteria for a response"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT AVG(score) as avg_score
            FROM evaluations
            WHERE response_id = ?
        ''', (response_id,))

        result = cursor.fetchone()
        conn.close()

        return result[0] if result[0] else 0

    def llm_evaluate(self, response_text, prompt_text, criteria, llm_client, db_path='llm_judge.db'):
        """
        Use an LLM to evaluate a response

        Args:
            response_text: The response to evaluate
            prompt_text: The original prompt
            criteria: Single criterion to evaluate (e.g., "clarity")
            llm_client: LLMClient instance to use for judging

        Returns:
            tuple: (score, feedback)
        """
        judge_prompt = f"""You are evaluating an AI response based on the criterion: {criteria}

Original Prompt: {prompt_text}

Response to Evaluate:
{response_text}

Rate the response on {criteria} from 0-10 and provide brief feedback.

Respond in exactly this format:
Score: [number 0-10]
Feedback: [one sentence]"""

        llm_response = llm_client.get_response(judge_prompt, max_tokens=200)

        # Parse the score and feedback
        lines = llm_response.strip().split('\n')
        score = None
        feedback = None

        for line in lines:
            if line.startswith('Score:'):
                try:
                    score = int(line.split(':')[1].strip())
                except:
                    score = 5  # Default if parsing fails
            elif line.startswith('Feedback:'):
                feedback = line.split(':', 1)[1].strip()

        return (score or 5, feedback or "No feedback provided")

# Test removed - not needed anymore