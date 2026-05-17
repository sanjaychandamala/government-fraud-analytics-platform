
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Government Fraud Analytics API Running"}

@app.get("/fraud-score")
def fraud_score():
    return {
        "transaction_id": 10021,
        "risk_score": 0.92,
        "status": "High Risk"
    }
