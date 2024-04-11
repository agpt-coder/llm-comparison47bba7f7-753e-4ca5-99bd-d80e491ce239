import logging
from contextlib import asynccontextmanager

import project.generate_response_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="LLM Comparison",
    lifespan=lifespan,
    description='To create an API endpoint `/api/generate-response` that meets the project requirements, follow these steps with the specified tech stack:\n\n1. **Setup FastAPI**: Initialize a new FastAPI application. FastAPI will serve as the web framework to create the API endpoint.\n\n2. **Endpoint Creation**:\n   - Define a new POST endpoint at `/api/generate-response`. This endpoint should accept JSON payload containing a `prompt` field.\n   - Use Pydantic models to ensure the input is properly validated.\n\n3. **Integration with Anthropic\'s Claude and OpenAI\'s GPT-4 Models**:\n   - For Claude, use the provided code snippet to send the `prompt` to Claude\'s API and wait for the response. Ensure you have the Anthropics SDK installed (`pip install anthropic`).\n   - Similarly, for GPT-4, use the OpenAI SDK (`pip install openai`) with the provided code to send the `prompt` and receive the response.\n\n4. **Processing Responses**:\n   - Once responses are received from both models, construct a JSON object containing the responses from Claude and GPT-4. The object should match the desired output structure:\n```json\n{\n  "claude_response": "Claude\'s actual response",\n  "gpt4_response": "GPT-4\'s actual response"\n}\n```\n   - Ensure to replace `Claude\'s actual response` and `GPT-4\'s actual response` with the actual responses received from the APIs.\n\n5. **Return the Combined Response**:\n   - Send the constructed JSON as the response to the client making the POST request to `/api/generate-response`.\n\n**Tech Stack Implementation**: \n- Utilize Python as the programming language to implement the logic.\n- Use FastAPI for setting up the API endpoint and handling HTTP requests.\n- Although the primary task does not require database interaction or ORM utilization, PostgreSQL and Prisma are available in the tech stack for potential extensions or data persistence needs related to storing prompts and responses for audit or logging purposes.',
)


@app.post(
    "/api/generate-response",
    response_model=project.generate_response_service.GenerateResponseOutput,
)
async def api_post_generate_response(
    prompt: str,
) -> project.generate_response_service.GenerateResponseOutput | Response:
    """
    Accepts a JSON payload with a 'prompt' field, sends requests to external AI APIs, and returns combined responses.
    """
    try:
        res = await project.generate_response_service.generate_response(prompt)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
