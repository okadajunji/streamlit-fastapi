import streamlit as st
import requests
import pandas as pd
from PIL import Image
import io
import os

# FastAPIのエンドポイント
# Streamlit Share の環境変数へ Render のデプロイURLを設定する
# 環境変数に RENDER_URL が設定されていない場合はデフォルトのURLを設定する
url = os.environ.get("RENDER_URL") or 'http://localhost:8000'

# レイアウトとタイトルの設定
st.set_page_config(layout="centered")
st.title("Streamlit & FastAPI")
st.write(url)

# CSVファイルの処理
st.header("CSVファイル処理(先頭5行の抽出)")
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, "multipart/form-data")}
    response = requests.post(f"{url}/process-csv/", files=files)
    if response.ok:
        st.write("ファイルを処理しました。先頭5行は以下の通りです：")
        df = pd.read_csv(io.StringIO(response.text))
        st.write(df)
    else:
        st.write("エラーが発生しました。")


# 画像ファイルの処理
st.header("画像ファイル処理(グレースケール)")
uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, "multipart/form-data")}
    response = requests.post(f"{url}/process-image/", files=files)
    if response.ok:
        st.write("画像をグレースケールに変換しました。")
        image = Image.open(io.BytesIO(response.content))
        st.image(image)
    else:
        st.write("エラーが発生しました。")