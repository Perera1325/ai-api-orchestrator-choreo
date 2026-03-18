from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Engine running on Choreo 🚀"}

@app.get("/analyze")
def analyze():
    return {
        "message": "AI orchestration endpoint working",
        "status": "success"
    }