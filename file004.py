from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <title>Chat Box</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: black;
                margin: 0;
                color: white;
                text-align: center;
            }
            .container {
                background: #222;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
                width: 90%;
                max-width: 400px;
            }
            h1 {
                color: white;
            }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: red;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }
            .btn:hover {
                background-color: darkred;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, this is my chat box. 😂</h1>
            <a class="btn" href="https://example.com">Rip your IQ 😂</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)
