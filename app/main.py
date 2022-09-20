from fastapi import FastAPI
import uvicorn

from api.v1 import v1
from api.v1.mock import mock


app = FastAPI()
app.include_router(v1.api_router, prefix='/api/v1')
app.include_router(mock.api_router, prefix='/api/v1/mock')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")