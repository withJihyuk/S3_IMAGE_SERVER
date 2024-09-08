import io, os, uuid
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from boto3 import client

app = FastAPI()
s3_client = client(
    "s3",
    endpoint_url=os.environ.get("S3_ENDPOINT"),
    aws_access_key_id=os.environ.get("S3_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET_KEY"),
    region_name=os.environ.get("S3_REGION"),
)


@app.post("/files/images")
def upload_images(file: UploadFile):
    max_file_size = 10 * 1024 * 1024  # 10MB
    file_name = uuid.uuid4().hex

    if file.size > max_file_size:
        return JSONResponse({"message": "파일 용량이 너무 큽니다."}, status_code=400)

    try:
        in_mem_file = io.BytesIO()
        Image.open(file.file).convert("RGBA").save(in_mem_file, "webp", quality=90)
        in_mem_file.seek(0)
    except Exception:
        return JSONResponse({"message": "업로드에 실패 했습니다."}, status_code=500)

    s3_client.put_object(
        Body=in_mem_file,
        Bucket="profile-images",
        Key=f"{file_name}.webp",
        ContentType="image/*",
    )
    return JSONResponse({"message": "업로드에 성공 했습니다.", "file_name": file_name})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
