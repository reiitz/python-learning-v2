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

# Test the classes
if __name__ == "__main__":
        # Create a prompt
        prompt = Prompt("Explain quantum computing in simple terms", category="explanation")
        prompt_id = prompt.save()
        print(f"✓ Prompt saved with ID: {prompt_id}")

        # Create a response
        response = Response(
            prompt_id=prompt_id,
            llm_provider="test_llm",
            response_text="Quantum computing uses quantum mechanics..."
        )
        response_id = response.save()
        print(f"✓ Response saved with ID: {response_id}")

        # Use Judge to evaluate
        judge = Judge(criteria_list=["clarity", "accuracy", "helpfulness"])

        scores = {
            "clarity": (8, "Clear explanation with good structure"),
            "accuracy": (7, "Technically correct but simplified"),
            "helpfulness": (9, "Very helpful for beginners")
        }

        eval_ids = judge.evaluate_response(response_id, scores)
        print(f"✓ Created {len(eval_ids)} evaluations: {eval_ids}")

        # Get average score
        avg = judge.get_average_score(response_id)
        print(f"✓ Average score: {avg:.2f}/10")

# Test the classes
if __name__ == "__main__":
    # Create a prompt
    prompt = Prompt("Explain quantum computing in simple terms", category="explanation")
    prompt_id = prompt.save()
    print(f"✓ Prompt saved with ID: {prompt_id}")

    # Create a response
    response = Response(
        prompt_id=prompt_id,
        llm_provider="test_llm",
        response_text="Quantum computing uses quantum mechanics..."
    )
    response_id = response.save()
    print(f"✓ Response saved with ID: {response_id}")

    # Create an evaluation
    evaluation = Evaluation(
        response_id=response_id,
        criteria="clarity",
        score=8,
        feedback="Good explanation but could use more examples"
    )
    eval_id = evaluation.save()
    print(f"✓ Evaluation saved with ID: {eval_id}")