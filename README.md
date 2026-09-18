# AI Resume Grader — CS AI Workshop Starter

You already have an application. Your job is to give it AI.

The Gradio frontend is finished. During the workshop, you will connect the app to Google Gemini in `ai.py`, then experiment with the grading prompt in `prompt.py`.

## What you need

- Python 3.9 or newer
- A Gemini API key from Google AI Studio: https://aistudio.google.com/api-keys

## 1. Open a terminal in this folder

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 2. Add your API key

Copy `.env.example` to a new file named `.env`.

macOS / Linux:

```bash
cp .env.example .env
```

Then put your own key in `.env`:

```text
GEMINI_API_KEY=your_actual_key_here
```

Never post your key in Discord or push it to GitHub.

## 3. Run the starter app

```bash
python app.py
```

Open the local Gradio URL printed in your terminal. The interface should run, but clicking **Grade Resume** will say the AI is not implemented yet. That is intentional.

## 4. Your task

Open `ai.py` and work through the TODOs:

1. Read `GEMINI_API_KEY` from the environment.
2. Import `genai` from Google and create a Gemini client.
3. Import and call `build_grading_prompt` from `prompt.py`.
4. Send the prompt to Gemini.
5. Return Gemini's text response to the frontend.

Then open `prompt.py` and make the grader your own. Change the rubric, tone, categories, or requested feedback and see how the output changes.

## Project flow

```text
Resume text
   ↓
Gradio frontend (`app.py`)
   ↓
Python function (`ai.py`)
   ↓
Gemini API
   ↓
Gemini model
   ↓
AI response
   ↓
Gradio displays feedback
```

## Test resumes

Use any file inside `sample_resumes/` to test your grader.

## Optional extensions

- Compare a resume to a job description
- Add category scores
- Add PDF upload
- Save past results
- Create a job-match analyzer
- Later connect outside tools/data through MCP
