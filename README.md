## S3_IMAGE_SERVER

FastAPI + boto3 + PIL로 이루어진 이미지 업로드 서버입니다.   
엔드포인트로 업로드한 이미지를 .webp 확장자로 변환 하여 s3 버킷에 저장하도록 도와줍니다.

### 사용법
```
export S3_ENDPOINT=(본인의 값)
export S3_ACCESS_KEY=(본인의 값)
export S3_SECRET_KEY=(본인의 값)
export S3_REGION=(본인의 값)

pip install -r requirements.txt
python3 main.py
```