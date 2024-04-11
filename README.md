---
date: 2024-04-11T11:34:29.530041
author: AutoGPT <info@agpt.co>
---

# LLM Comparison

To create an API endpoint `/api/generate-response` that meets the project requirements, follow these steps with the specified tech stack:

1. **Setup FastAPI**: Initialize a new FastAPI application. FastAPI will serve as the web framework to create the API endpoint.

2. **Endpoint Creation**:
   - Define a new POST endpoint at `/api/generate-response`. This endpoint should accept JSON payload containing a `prompt` field.
   - Use Pydantic models to ensure the input is properly validated.

3. **Integration with Anthropic's Claude and OpenAI's GPT-4 Models**:
   - For Claude, use the provided code snippet to send the `prompt` to Claude's API and wait for the response. Ensure you have the Anthropics SDK installed (`pip install anthropic`).
   - Similarly, for GPT-4, use the OpenAI SDK (`pip install openai`) with the provided code to send the `prompt` and receive the response.

4. **Processing Responses**:
   - Once responses are received from both models, construct a JSON object containing the responses from Claude and GPT-4. The object should match the desired output structure:
```json
{
  "claude_response": "Claude's actual response",
  "gpt4_response": "GPT-4's actual response"
}
```
   - Ensure to replace `Claude's actual response` and `GPT-4's actual response` with the actual responses received from the APIs.

5. **Return the Combined Response**:
   - Send the constructed JSON as the response to the client making the POST request to `/api/generate-response`.

**Tech Stack Implementation**: 
- Utilize Python as the programming language to implement the logic.
- Use FastAPI for setting up the API endpoint and handling HTTP requests.
- Although the primary task does not require database interaction or ORM utilization, PostgreSQL and Prisma are available in the tech stack for potential extensions or data persistence needs related to storing prompts and responses for audit or logging purposes.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'LLM Comparison'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
