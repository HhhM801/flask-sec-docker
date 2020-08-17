from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def test():
    template = '''
        <div>
            <h3>%s</h3>
        </div>
    ''' % (request.args.get("a"))

    return render_template_string(template)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)