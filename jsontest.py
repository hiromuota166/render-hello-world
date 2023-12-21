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

    data = []

    time_rows = soup.select('tr.item_base')
    status_rows = soup.select('tr.tr_base')
    
    # 同じインデックスの行から時刻とステータスを抽出
    for time_row, status_row in zip(time_rows, status_rows):
        time_cells = time_row.find_all('td')
        status_cells = status_row.find_all('td')

        for time_cell, status_cell in zip(time_cells, status_cells):
            #時刻の処理
            time_text = time_cell.get_text(strip=True).replace('\uff1a', ':').replace('\u301c', '-')

            #ステータスの処理
            img = status_cell.find('img')
            if img:
                if 'msg_icon05.gif' in img['src']:
                    status = 'O'
                elif 'msg_icon01.gif' in img['src']:
                    status = 'X'
                else:
                    status = '?'
            else:
                status = 'None'

            data.append({
                'time': time_text,
                'status': status
            })
    return jsonify(data)
    
if __name__ == '__main__':
    app.run()