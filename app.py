from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello,world'


@app.route('/login/<id>/<password>', methods=['post', 'get'])
def login(idNum, password):
    if idNum == '20301038':
        if password == '123456':
            return '登陆成功'
        else:
            return '登陆失败'


@app.route('/queryInfo')
def getinfo():
    infomation = Placetb.query.all()
    if infomation is None:
        return '查询失败'
    else:
        return infomation


if __name__ == '__main__':
    app.run()
