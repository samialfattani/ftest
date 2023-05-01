from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# if __name__ == "__main__":
#     app.run()

if __name__ == '__main__':
    from waitress import serve
    p = os.environ.get('PORT')
    p = p if p else '5051'
    print('ok')
    serve(app, host='0.0.0.0', port=p)