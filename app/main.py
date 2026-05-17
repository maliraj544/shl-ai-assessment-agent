from fastapi import FastAPI
from pydantic import BaseModel

from app.recommender import recommend_assessments

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/recommend")
def recommend(request: QueryRequest):

    result = recommend_assessments(
        request.query
    )

    return {
        "query": request.query,
        "recommendations": result["recommendations"],
        "explanation": result["explanation"]
    }