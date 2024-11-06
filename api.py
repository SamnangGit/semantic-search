from fastapi import FastAPI
from rerank_response import RankLLM
import cohere

app = FastAPI()

@app.get("/")
def rerank():
    rankLLM = RankLLM()
    return rankLLM.main().results[0]