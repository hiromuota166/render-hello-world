from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = 'https://www.yomiuri.co.jp'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.title.string