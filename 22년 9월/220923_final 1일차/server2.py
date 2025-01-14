 # -*- coding: utf-8 -*-

from flask import Flask
import random

app = Flask(__name__)

# 보통 topics에 저장되있는건 DB를 연동해서 하는데 나중에 찾아보기
topics = [
    {'id' : 1, 'title' : 'html', 'body' : 'html is ...'},
    {'id' : 2, 'title' : 'css', 'body' : 'css is ...'},
    {'id' : 3, 'title' : 'javascript', 'body' : 'javascript is ...'}
 ]

def template(contents, content) : 
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}  
            <ul>
                <li><a herf="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def getContents() :
    liTags = ''
    for topic in topics : 
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index() :
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')
def read(id) :    
    title = ''
    body = ''
    for topic in topics :
        if id == topic['id'] :
            title = topic['title']
            body = topic['body']
            break
        print(title, body)
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
     '''
    return template(getContents(), content)



app.run(debug=True) # 5000port를 이용하고, 새로고침하면 반영