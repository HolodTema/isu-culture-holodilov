from fastapi import FastAPI, HTTPException, Query

app = FastAPI(title="Fibonacci API", version="0.0.1")

def fibonacci(n: int) -> list:
    if n < 1:
        raise ValueError("n must be >= 1")
    seq = [0]
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
        b = a + b
        a = b
        seq.append(b)
    return seq


@app.get("/fiblist")
def get_fibonacci_list(n: int = Query(10, ge=1, le=200, description="Amount numbers")) -> dict:
    try:
        values = fibonacci(n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"n": n, "values": values}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

