# main.py
from web import product
from fastapi import FastAPI
from web import login
from web import seller

app = FastAPI()

# 라우터 등록
app.include_router(login.router)
app.include_router(product.router)
app.include_router(seller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)