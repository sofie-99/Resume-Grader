"""The workshop file: connect this app to Gemini here."""


def grade_resume(resume_text: str) -> str:
    """Return resume feedback for the text entered in the Gradio app."""
    if not resume_text or not resume_text.strip():
        return "Please paste a resume before grading it."

    # TODO 1: Read GEMINI_API_KEY from the environment (or load it from .env).
    # TODO 2: Import `genai` from `google` and initialize a Gemini client.
    # TODO 3: Import and call `build_grading_prompt` from prompt.py.
    # TODO 4: Send the finished prompt and resume text to a Gemini model.
    # TODO 5: Extract the model's text response and return it below.
    # Tip: Keep this function small. It only needs to send one request and return text.

    return "AI functionality has not been implemented yet. Connect the Gemini API in ai.py!"
