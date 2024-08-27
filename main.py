from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/health")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
