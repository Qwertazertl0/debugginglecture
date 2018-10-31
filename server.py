from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

dic = {}
reverse_dic = {}
last_number = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_shortened_url():
    global last_number
    data = request.form['url']
    if data in dic.values():
        print("http://127.0.0.1:5000/" + str(reverse_dic[data]))
    else: 
        dic[last_number] = data
        reverse_dic[data] = last_number
        print("http://127.0.0.1:5000/" + str(last_number))
    return render_template('index.html')

@app.route('/<url_alias>')
def redirect_to_original_url(url_alias):
    original_url = dic[int(url_alias)]
    return redirect(original_url, code=302)

if __name__ == '__main__':
    app.run(debug = True)
