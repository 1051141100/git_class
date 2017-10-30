from flask import Flask,render_template,request,redirect,url_for,session,make_response,get_flashed_messages,message_flashed,flash,views

app = Flask(__name__,static_folder='static',static_url_path="/ppppp")

app.secret_key = "asdfasdfaksdufpoiuasdkfnasidf"


DB = {
    "1": ['赵凤凤','女'],
    "2": ['银秋良','女'],
    "3": ['吴一飞','女'],
}

@app.route('/login',methods=['GET','POST'])
def login():
    # print(request.method)
    # print(request.args)
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('username')
        pwd = request.form.get('password')

        if user == 'alex' and pwd == '123':
            # return redirect('http://www.baidu.com')
            # return redirect('/indexxxxxxxx')
            session['user_info'] = 'alex'
            return redirect(url_for('index'))
        else:
            return render_template('login.html',msg="用户名或密码")

@app.route('/indexxxxxxxx',methods=['GET',])
def index():
    if not session.get('user_info'):
        return redirect(url_for('login'))

    return render_template('index.html',data_list=DB)

def func(a1,a2):
    return "<a href='http://www.baidu.com'>百度云</a>"

@app.route('/detail/<nid>',methods=['GET',])
def detail(nid):
    if not session.get('user_info'):
        return redirect(url_for('login'))

    user_detail = DB[nid]
    return render_template('detail.html',**{'user_detail':user_detail,'func':func})

@app.route('/test1')
def test1():
    val = request.args.get('p')
    flash(val)
    return "test1"


@app.route('/test2')
def test2():
    messages = get_flashed_messages()
    print(messages)
    return "test2"


if __name__ == '__main__':
    app.run()