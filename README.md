# 概要
StreamlitとFastAPIでCSVファイルと画像ファイルを扱う最小限のコードです。

## 必要なライブラリ
```
fastapi
streamlit
pandas
Pillow
```

以下のコマンドでインストールすることができます。

```
pip install -r requirements.txt
```

## StreamlitとFastAPIの機能の切り分けの考え方
・主な機能はすべてFastAPIで実装し、FastAPIで出来ない部分をStreamlitで実装する。

・FastAPIで出来ない部分とは、ユーザーとのデータのやり取りの部分です。

・今回の場合では、ユーザーからのファイルの取得や処理結果の表示をStreamlitで実装しています。
