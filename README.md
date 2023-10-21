# 概要
StreamlitとFastAPIでCSVファイルと画像ファイルを扱う最小限のコードです。

## StreamlitとFastAPIの機能の切り分けの考え方
・主な機能はすべてFastAPIで実装し、FastAPIで出来ない部分をStreamlitで実装する。

・FastAPIで出来ない部分とは、ユーザーとのデータのやり取りの部分です。

・今回の場合では、ユーザーからのファイルの取得や処理結果の表示をStreamlitで実装しています。

## 必要なライブラリ
`requirements.txt`に記載しています。

以下のコマンドでインストールすることができます。

```
pip install -r requirements.txt
```

## ローカルでの実行コマンド
FastAPI
```
uvicorn main:app
```

Streamlit
```
streamlit run streamlit_app.py
```

# デプロイ

## FastAPI側をRenderへデプロイする

①『New＋』をクリック<br>
②『Web Service』をクリック<br>
![step1](images/render_01.png)

③『Next』をクリック<br>
![step2](images/render_02.png)

④デプロイするリポジトリの『Connect』をクリック<br>
![step3](images/render_03.png)

⑤『Name』に任意のアプリ名を入力する（デプロイ時のURLに使われる）<br>
⑥『Start Command』に`uvicorn main:app --host 0.0.0.0 --port 10000`を入力する<br>
<a style="color:orange;">※このコマンドによりFastAPI側のmain.pyが実行される</a>
![step4](images/render_04.png)

⑦『Create Web Service』をクリックする<br>
![step5](images/render_05.png)

⑧アプリの起動を確認する<br>
⑨『デプロイURL』をクリックする<br>
![step6](images/render_06.png)

`{"message":"Hello World"}`と表示されていれば成功！<br>
![step7](images/render_07.png)

これは以下の部分が対応している。<br>
https://github.com/okadajunji/streamlit-fastapi/blob/9ef24efd0d4da2e109f28c3242a60732967e89b9/main.py#L10-L13

## Streamlit側をStreamlitShareへデプロイする

①『New app』をクリック<br>
![step1](images/streamlitshare_01.png)

②デプロイするリポジトリをクリック<br>
③公開するアプリURLを設定する<br>
④『Advanced settings...』をクリック<br>
⑤『Secrets』に以下の内容を入力<br>
　（`[your-app-name]`の部分は『FastAPI側をRenderへデプロイする』の⑨を参照）
```
[general]
RENDER_URL = "https://[your-app-name].onrender.com/"
```
⑥『Save』をクリック<br>
⑦『Deploy!』をクリック<br>
![step2](images/streamlitshare_02.png)

CSVファイルや画像ファイルをアップロードして動作すれば成功！<br>
![step3](images/streamlitshare_03.png)

# 以上、おつかれさまでした！！