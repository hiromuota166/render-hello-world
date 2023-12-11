from flask import Flask
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def hello_world():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.reserve1.jp/yoyaku/member/MemberReserve.php?mn=2&lc=wrxqxwrrxx&gr=2&stt=MLRRX")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()  # ブラウザを閉じる
    return soup.prettify()  # HTMLコンテンツを整形して文字列として返す
