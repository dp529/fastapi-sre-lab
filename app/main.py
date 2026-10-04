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
