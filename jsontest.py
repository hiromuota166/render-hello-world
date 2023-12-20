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
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    # 時刻を抽出する
    # time_slots = soup.select('tr.item_base td:nth-of-type(2)')
    # times = ['~'.join(td.stripped_strings) for td in time_slots]

    print(soup)

    # # 空き状況を抽出する
    # for row in enumerate(soup.select('tr.tr_base')):
    #     cells = row.find_all('td')[1:]  # 最初のtd（コート名）をスキップ
    #     for i, cell in enumerate(cells):
    #         if cell.find('img', src="p_img/msg_icon05.gif"):
    #             status = "空"
    #         elif cell.find('img', src="p_img/msg_icon01.gif"):
    #             status = "満"
    #         else:
    #             status = "？"

    #         data.append({
    #             "time": times[i],
    #             "court": cell.get_text(strip=True),
    #             "status": status
    #         })

    return jsonify(data)

if __name__ == '__main__':
    jsontest()