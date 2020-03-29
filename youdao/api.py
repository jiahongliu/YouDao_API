'''
接口
'''
from YouDao import run
from flask import Flask, request
import json

app = Flask(__name__)

# 只接受get方法访问
@app.route("/test", methods=["GET"])
def check():
    if request.args is None:
        return '请求参数为空'
    word=request.args.get('word')
    return run(word)

if __name__ == '__main__':
    app.run()




