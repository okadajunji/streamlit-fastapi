from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import pandas as pd
from PIL import Image
import io

app = FastAPI()


@app.post("/process-csv/")
async def process_csv(file: UploadFile = File(...)):
    # ファイル内容をDataFrameに読み込む
    dataframe = pd.read_csv(file.file)
    # 先頭5行を抽出
    result = dataframe.head()
    # 結果を文字列（CSV形式）に変換して返す
    stream = io.StringIO()
    result.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response


@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # 画像ファイルの読み込みとグレースケール変換
    image = Image.open(file.file).convert('L')
    # 画像をバイトデータに変換してレスポンスとして返す
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return StreamingResponse(io.BytesIO(img_byte_arr.getvalue()), media_type="image/png")