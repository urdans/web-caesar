from flask import Flask, request
from caesar import encrypt as rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
<head>
    <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }

        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
    </style>
</head>
<body>
    <form method="POST">
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
            <p></p><br>
        </div>
        <textarea type="text" name="text"></textarea>
        <p></p><br>
        <div>
            <input type="submit" value="Encrypt">
        </div>
    </form>
</body>
</html>
"""


@app.route("/", methods=['POST'])
def encrypt():
    if request.method == 'POST':
        rotation = request.form["rot"]
        message = request.form["text"]
        encrypted_msg = rotate_string(message, int(rotation))
        print(message)
        print(encrypted_msg)
    return '<h1>{}</h1>'.format(encrypted_msg)


@app.route("/")
def index():
    return form


app.run()
