from fastapi import FastAPI

app = FastAPI(title="Voice AI Clinical Agent")

@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}