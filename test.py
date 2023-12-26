from flask import Flask
import requests
from flask_cors import CORS
from flask import request
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def apptest():
    # リクエストのURL
    url = "https://www.reserve1.jp/yoyaku/member/member_job_select.php"

    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")

    year = request.args.get('year', default=current_year)
    month = request.args.get('month', default=current_month)
    day = request.args.get('day', default=current_day)

    date_key = f"c_b[{year}{month}]"
    # リクエストに必要なペイロードを設定
    payload = {
        "office":"4000393",
        "proc_flg":"SMRRX",
        "m_button":"",
        "member":"0",
        "grand":"2",
        "mngfg":"2",
        "c_month":"1", # 変更が必要
        date_key: day, # 変更が必要:日付を指定する
        # "in_select":"3", # 変更が必要
        # "SID":"l033042i9o7dkjlj2u2ap9vqkhao9tnu",
        # "selecode_rec":"",
        # "in_dd_select":"26",
        # "ym_select":"1",
    }

    # POSTリクエストを送信
    response = requests.post(url, data=payload)
    return response.text

    # レスポンス内容を確認
    # print(response.text)

if __name__ == "__main__":
    app.run(debug=True)
