import os
from dotenv import load_dotenv
from google import genai
from prompt import build_grading_prompt

def grade_resume(resume_text: str) -> str:
    if not resume_text or not resume_text.strip():
        return "Please paste a resume before grading it."

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Missing GEMINI_API_KEY"

    client = genai.Client(api_key=api_key)
    prompt = build_grading_prompt(resume_text)

    response = client.interactions.create(
        model = "gemini-3.8-flash",
        input = prompt,
    )

    return response.output_text