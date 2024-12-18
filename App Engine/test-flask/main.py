# flask 是 python 最基本的一個網頁框架
from flask import Flask
app = Flask(__name__)

@app.route("/") # 當使用者輸入這個路徑後回傳下列內容
def hello():
    return "Hello, World! 2024/7/22"

if __name__ == "__main__":
    app.run(debug=True) #執行部分從app run開始
