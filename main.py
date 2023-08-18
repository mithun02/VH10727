from fastapi import FastAPI, Query
from typing import List, Any
import requests

app = FastAPI()


@app.get("/numbers")
async def numbers(url:  List[str] = Query(..., description="List of URLs")) -> List[dict]:

    responses = []
    for link in url:
        try:
            resp = requests.get(url=link, timeout=500/1000)
            responses.append(resp.json())
        except Exception as e:
            print(e)
    return responses