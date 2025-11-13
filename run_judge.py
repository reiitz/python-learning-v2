from llm_judge_models import Prompt, Response, Judge
from llm_client import LLMClient

def run_evaluation(prompt_text, criteria_list):
    """
    Complete workflow: prompt -> LLM response -> evaluation
    """
    print(f"📝 Prompt: {prompt_text}\n")

    # 1. Save prompt to database
    prompt = Prompt(prompt_text, category="test")
    prompt_id = prompt.save()
    print(f"✓ Prompt saved (ID: {prompt_id})")

    # 2. Get LLM response
    client = LLMClient()
    response_text = client.get_response(prompt_text)
    print(f"\n🤖 Claude Response:\n{response_text}\n")

    # 3. Save response
    response = Response(
        prompt_id=prompt_id,
        llm_provider="claude-sonnet-4",
        response_text=response_text
    )
    response_id = response.save()
    print(f"✓ Response saved (ID: {response_id})")

    # 4. Manual scoring (we'll automate this next)
    print(f"\n⚖️  Now scoring the response...")

    # For now, let's use fixed scores as an example
    judge = Judge(criteria_list)

    # You would normally evaluate these manually or with another LLM
    # For demo, using placeholder scores
    scores = {}
    for criterion in criteria_list:
        scores[criterion] = (8, f"Good performance on {criterion}")

    eval_ids = judge.evaluate_response(response_id, scores)
    print(f"✓ Created {len(eval_ids)} evaluations")

    # Get average score
    avg = judge.get_average_score(response_id)
    print(f"✓ Average score: {avg:.2f}/10")

    return prompt_id, response_id

if __name__ == "__main__":
    # Test the full workflow
    test_prompt = "Explain quantum entanglement in simple terms for a high school student"
    criteria = ["clarity", "accuracy", "simplicity"]

    run_evaluation(test_prompt, criteria)