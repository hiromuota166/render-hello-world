from flask import Flask
from selenium import webdriver
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_danjyo():
    driver = webdriver.Chrome()
    driver.get('https://www.reserve1.jp/yoyaku/member/MemberReserve.php?mn=2&lc=wrxqxwrrxx&gr=2&stt=MLRRX')

    soup = BeautifulSoup(driver.page_source, 'html.parser').text
    return soup