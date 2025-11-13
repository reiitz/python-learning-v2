from llm_judge_models import Prompt, Response, Judge
from llm_client import LLMClient

def run_evaluation_with_llm_judge(prompt_text, criteria_list):
    """
    Complete workflow with LLM-as-judge for automated scoring
    """
    print(f"📝 Prompt: {prompt_text}\n")

    # 1. Save prompt
    prompt = Prompt(prompt_text, category="test")
    prompt_id = prompt.save()
    print(f"✓ Prompt saved (ID: {prompt_id})")

    # 2. Get response from Claude
    client = LLMClient()
    response_text = client.get_response(prompt_text)
    print(f"\n🤖 Claude Response:\n{response_text[:200]}...\n")

    # 3. Save response
    response = Response(
        prompt_id=prompt_id,
        llm_provider="claude-sonnet-4",
        response_text=response_text
    )
    response_id = response.save()
    print(f"✓ Response saved (ID: {response_id})")

    # 4. Use LLM to judge the response
    print(f"\n⚖️  Using Claude to evaluate on {len(criteria_list)} criteria...\n")

    judge = Judge(criteria_list)
    scores = {}

    for criterion in criteria_list:
        print(f"  Evaluating {criterion}...", end=" ")
        score, feedback = judge.llm_evaluate(
            response_text=response_text,
            prompt_text=prompt_text,
            criteria=criterion,
            llm_client=client
        )
        scores[criterion] = (score, feedback)
        print(f"{score}/10")
        print(f"    → {feedback}")

    # 5. Save all evaluations
    eval_ids = judge.evaluate_response(response_id, scores)
    print(f"\n✓ Saved {len(eval_ids)} evaluations to database")

    # 6. Calculate average
    avg = judge.get_average_score(response_id)
    print(f"✓ Overall Average Score: {avg:.2f}/10")

    return prompt_id, response_id

if __name__ == "__main__":
    test_prompt = "Explain blockchain technology to someone who knows nothing about computers"
    criteria = ["clarity", "accuracy", "accessibility"]

    run_evaluation_with_llm_judge(test_prompt, criteria)