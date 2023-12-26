from flask import Flask , jsonify
import requests
from flask_cors import CORS
from bs4 import BeautifulSoup
from datetime import datetime
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/')
def appjson():

    url = "https://www.reserve1.jp/yoyaku/member/member_job_select.php"

    # 現在の日付を取得
    now = datetime.now()
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")

    # リクエストパラメータを取得（デフォルト値を現在の日付に設定）
    year = request.args.get('year', default=current_year)
    month = request.args.get('month', default=current_month)
    day = request.args.get('day', default=current_day)

    # ペイロード内の日付を動的に設定
    date_key = f"c_b[{year}{month}]"
    payload = {
        "office":"4000393",
        "proc_flg":"SMRRX",
        "m_button":"",
        "member":"0",
        "grand":"2",
        "mngfg":"2",
        date_key: day,  # 日付を動的に設定
        "c_month": "1",
    }

    # POSTリクエストを送信
    response = requests.post(url, data=payload)
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')

    # 手書きで時間帯を定義
    times = ["09:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00", "19:00-20:00", "20:00-21:00"]

    data = []

    # ステータス行を抽出する
    status_rows = soup.select('tr.tr_base')

    # 各時間帯に対して処理
    for time_index, time in enumerate(times):
        status_dict = {'time': time}

        # 各コートのステータスを取得
        for status_index, status_row in enumerate(status_rows):
            status_cell = status_row.find_all('td')[time_index + 1]  # 各時間帯に対応するtd
            img = status_cell.find('img')
            if img:
                if 'msg_icon05.gif' in img['src']:
                    status = 'O'
                elif 'msg_icon01.gif' in img['src']:
                    status = 'X'
                else:
                    status = '?'
            else:
                status = 'Error'
            status_dict[f'status{status_index + 1}'] = status

        data.append(status_dict)

    return jsonify(data)
    
if __name__ == '__main__':
    app.run()