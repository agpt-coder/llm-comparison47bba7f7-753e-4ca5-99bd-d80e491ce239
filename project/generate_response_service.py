import httpx
from pydantic import BaseModel


class GenerateResponseOutput(BaseModel):
    """
    Consolidated AI responses from both Claude and GPT-4.
    """

    claude_response: str
    gpt4_response: str


async def fetch_claude_response(prompt: str) -> str:
    """
    Fetches the response from Claude AI API for the given prompt. This function represents an async HTTP
    request to Claude's server.

    Args:
        prompt (str): The prompt to send to Claude AI.

    Returns:
        str: The response from Claude AI.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.claude.ai/call", json={"prompt": prompt}
        )
        result = response.json()
        return result.get("response", "")


async def fetch_gpt4_response(prompt: str) -> str:
    """
    Fetches the response from OpenAI's GPT-4 API for the given prompt. This function represents an async HTTP
    request to OpenAI's API.

    Args:
        prompt (str): The prompt to send to GPT-4 API.

    Returns:
        str: The response from GPT-4.
    """
    openai_api_key = "your_openai_api_key_here"
    headers = {"Authorization": f"Bearer {openai_api_key}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v4/completions",
            headers=headers,
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 256,
            },
        )
        result = response.json()
        return result["choices"][0]["text"] if result["choices"] else ""


async def generate_response(prompt: str) -> GenerateResponseOutput:
    """
    Accepts a JSON payload with a 'prompt' field, sends requests to external AI APIs, and returns combined responses.

    Args:
        prompt (str): Text prompt to generate AI-based responses.

    Returns:
        GenerateResponseOutput: Consolidated AI responses from both Claude and GPT-4.
    """
    claude_response = await fetch_claude_response(prompt)
    gpt4_response = await fetch_gpt4_response(prompt)
    return GenerateResponseOutput(
        claude_response=claude_response, gpt4_response=gpt4_response
    )
