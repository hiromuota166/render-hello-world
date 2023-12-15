from flask import Flask
import requests
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    # リクエストのURL
    url = "https://www.reserve1.jp/yoyaku/member/member_job_select.php"

    # リクエストに必要なペイロードを設定
    payload = {
        "office": "4000393",
        "grand": "2",
        "mngfg": "2",
        "rdate": "",  # 必要に応じて値を設定
        "wk_month": "",  # 必要に応じて値を設定
        "member": "",  # 必要に応じて値を設定
        "SID": "",  # 必要に応じて値を設定
        "proc_flg": "SMRRX"
    }

    # POSTリクエストを送信
    response = requests.post(url, data=payload)
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 特定のテーブルを取得
    table = soup.find('table', {'class': 'table_base'})

    if table:
        # 各々の画像を特定し、置換する
        for img in table.find_all('img'):
            if img['src'] == 'p_img/msg_icon01.gif':
                img.replace_with('❌')
            elif img['src'] == 'p_img/msg_icon05.gif':
                img.replace_with('⭕️')

    # テーブルのHTMLを文字列として返す
    return print(str(table))

if __name__ == '__main__':
    hello_world()