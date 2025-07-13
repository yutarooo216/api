import json
import base64
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from rna_3d_prediction.function import create_rna_processing_job

# FastAPIアプリケーションの初期化
app = FastAPI()

# フロントとの連携
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Reactの開発URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# リクエストボディのスキーマ
class RNARequest(BaseModel):
    sequence: str  # RNA配列
    email: EmailStr  # ユーザーのメールアドレス

# ヘルスチェックエンドポイント
@app.get("/")
async def health_check():
    return {"status": "ok"}

# RNA配列を受け取ってHelmセットアップとJobを作成するエンドポイント
@app.post("/submit-job/")
def submit_job(request: RNARequest):
    email=request.email
    # RNA処理用のJobを作成
    return create_rna_processing_job(rna_sequence=request.sequence, email=request.email)