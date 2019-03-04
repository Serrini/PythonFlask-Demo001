#encoding: utf-8

from flask import Flask, url_for, redirect, render_template
#url反转：由视图函数获得对应的url,需要import url_for
#redirect 重定向
#render_template templates文件夹下的html文件
import config
app = Flask(__name__)
app.config.from_object(config)


#注册url，主页面
@app.route('/')
def hello_world():
    print url_for('article',id='')
    #id='' 不可省略，此步为url反转

    login_url = url_for('login')
    return redirect(login_url)
    #此两步为页面跳转与重定向——>login界面
    #url_for()里面为视图函数名字
    #login_url用于接收由视图函数获得的对应url，此步为url反转


@app.route('/article/<id>')
def article(id):
    return u'您请求的参数是：%s' % id
#url传参：参数需要放在<>中，视图函数中需要放与url中参数同名的参数，即id



@app.route('/question/<is_logined>')
def question(is_logined):
    if is_logined == '1':
        return u'这是提问页面'
    else:
        return redirect(url_for('login'))

#注册url，登陆页面
@app.route('/login')
def login():
    return u'这是登陆界面'
#用于测试进入hello界面后，重定向到hello界面

@app.route('/login_info/<is_logined>')
def login_info(is_logined):
    if is_logined == '1':
        user = {
            'username': u'serrini',
            'age': 18
        }
        websites = ['www.baidu.com','www.google.com']
        for k,v in user.items():
            print k
            print v
        #python for循环遍历字典
        return render_template('login_info.html', user = user, websites = websites)
    else:
        return render_template('login_info  .html')



#注册url，个人信息页面
@app.route('/homepage')
def homepage():
    class Person(object):
        name = u'serrini'
        age = 16

    p = Person()

    context = {
        'username': u'sunlan',
        'gender': u'female',
        'age': u'18',
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)

#   return render_template('index.html', username=u'sunlan')
# 渲染Janja2模版用render_template函数，若html文件在templates文件下文件夹中，需添加路径。another/index.html
# 此句返回html文件，username由后端传回前端html文件，html文件中用{{username}}接收
# 模版传参：多个变量用字典


if __name__ == '__main__':
    app.run()
