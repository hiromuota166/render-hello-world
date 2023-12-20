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

    # 時刻を抽出する
    for row in soup.select('tr.item_base'):
      for cell in row.find_all('td'):
        text = cell.get_text(strip=True)
        # ユニコード文字の置換
        text = text.replace('\uff1a', ':').replace('\u301c', '-')
        data.append({
          'time': text
        })

    return jsonify(data)
    
if __name__ == '__main__':
    app.run()