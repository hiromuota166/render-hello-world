from flask import Flask
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def hello_world():
    options = Options()
    options.headless = True  # ヘッドレスモード True=非表示, False=表示
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.reserve1.jp/yoyaku/member/MemberReserve.php?mn=2&lc=wrxqxwrrxx&gr=2&stt=MLRRX")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup