from fastapi import FastAPI
from mongodb_config import counter_collection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# 초기 카운트 생성
if counter_collection.count_documents({}) == 0:
    counter_collection.insert_one({"_id": "counter", "count": 0})

@app.get("/count")
def get_count():
    counter = counter_collection.find_one({"_id": "counter"})
    if counter is None:
        raise HTTPException(status_code=404, detail="Counter not found")
    return {"count": counter["count"]}


@app.post("/increment")
def increment_count():
    counter_collection.update_one({"_id": "counter"}, {"$inc": {"count": 1}})
    return {"message": "Counter incremented"}


@app.post("/decrement")
def decrement_count():
    counter_collection.update_one({"_id": "counter"}, {"$inc": {"count": -1}})
    return {"message": "Counter decremented"}

@app.get("/")
def read_root():
    return {"message": "Hello, Docker with FastAPI!"}



# import os
# from back.mongodb_config import db
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()



# # CORS 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 모든 출처에서 요청 허용
#     allow_credentials=True,
#     allow_methods=["*"],  # 모든 HTTP 메소드 허용
#     allow_headers=["*"],  # 모든 HTTP 헤더 허용
# )

