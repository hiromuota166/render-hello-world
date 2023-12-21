from flask import Flask , jsonify
import requests
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/')
def jsontest():
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