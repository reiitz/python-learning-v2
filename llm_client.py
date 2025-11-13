import anthropic
import os

class LLMClient:
    def __init__(self, api_key=None):
        """
        Initialize LLM client

        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env variable)
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set ANTHROPIC_API_KEY or pass api_key parameter")

        self.client = anthropic.Anthropic(api_key=self.api_key)

    def get_response(self, prompt_text, model="claude-sonnet-4-20250514", max_tokens=1024):
        """
        Get response from Claude

        Args:
            prompt_text: The prompt to send
            model: Model to use
            max_tokens: Maximum response length

        Returns:
            Response text as string
        """
        message = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt_text}
            ]
        )

        return message.content[0].text

# Test
if __name__ == "__main__":
    try:
        client = LLMClient()

        test_prompt = "Explain what a black hole is in one sentence."
        print(f"Prompt: {test_prompt}")
        print(f"\nResponse: {client.get_response(test_prompt)}")

    except ValueError as e:
        print(f"⚠ Error: {e}")