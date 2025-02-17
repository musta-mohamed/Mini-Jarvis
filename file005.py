from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "What up World."
    return render_template('hell_01.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
