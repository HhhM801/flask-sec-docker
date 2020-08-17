# -*- coding: utf-8 -*-
from flask import Flask,request,session,render_template_string
app = Flask(__name__)

app.secret_key = "hello world"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    session['user'] = 'tom'
    template = '''
        <div>
            <h3>%s</h3>
        </div>
    ''' % (request.args.get("a"))

    return render_template_string(template)


@app.route('/session', methods=['GET', 'POST'])
def sess():
    template = '''
        <div>
            <h3>%s</h3>
        </div>
    ''' % (session['user'])

    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)