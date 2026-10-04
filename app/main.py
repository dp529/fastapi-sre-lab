from fastapi import FastAPI
import socket

app = FastAPI(
    title="Order Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Order Service is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/orders")
def orders():
    return {
        "version": "v1",
        "hostname": socket.gethostname(),
        "orders": [
            {
                "id": 1,
                "item": "Laptop",
                "status": "SHIPPED"
            },
            {
                "id": 2,
                "item": "Monitor",
                "status": "PROCESSING"
            }
        ]
    }
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)

@app.get("/fail")
def fail():
    raise RuntimeError("intentional failure for SRE test")

@app.get("/cpu")
def cpu(seconds: int = 5):
    import time
    end = time.time() + seconds
    x = 0
    while time.time() < end:
        x += 1
    return {"status": "done", "iterations": x}
