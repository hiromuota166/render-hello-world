import requests

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

# レスポンス内容を確認
print(response.text)
