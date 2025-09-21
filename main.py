from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so Streamlit frontend can access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev only; specify domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/evaluate/")
async def evaluate_resume(
    title: str = Form(...),
    skills: str = Form(...),
    description: str = Form(...),
    resume: UploadFile = File(...)
):
    # Parse skills string to list
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]

    # Dummy evaluation logic (replace with your actual logic)
    score = 90.5
    verdict = "Strong Match"
    feedback = (
        f"Evaluated resume '{resume.filename}' against job '{title}'. "
        f"Skills matched: {', '.join(skills_list)}. "
        f"Description length: {len(description)} characters."
    )

    return {"score": score, "verdict": verdict, "feedback": feedback}
