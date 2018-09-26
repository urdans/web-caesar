from flask import Flask, request
from caesar import encrypt as rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
<head>
    <style>
        form {{
            background-color: rgb(85, 132, 141); 
            /*background-image: url("./images/camouflage.jpg");*/
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
        p {{
            color: rgb(126, 33, 33);
            font-size: 12px;
            font-style: italic;
        }}
        textarea {{
            margin: 10px 0;
            width: 532px;
            height: 120px;
            resize: none;
        }}
        label {{
            color:rgb(40, 51, 40);
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <form method="POST">
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="{rotation}">
            <p>{errormsg1}</p><br>
        </div>
        <textarea name="text">{textmsg}</textarea>
        <p>{errormsg2}</p><br>
        <div>
            <input type="submit" value="Encrypt">
        </div>
    </form>
</body>
</html>
"""


@app.route("/", methods=['POST'])
def encrypt():
    # global form2
    errormsg1 = ''
    errormsg2 = ''
    message = ''
    encrypted_msg = ''

    def render():
        return form.format(rotation=rotation, errormsg1=errormsg1, errormsg2=errormsg2, textmsg=encrypted_msg)

    if request.method == 'POST':
        try:
            rotation = request.form["rot"]
            message = request.form["text"]
        except Exception as E:
            errormsg1 = 'Error: ' + E.__str__() + '<br>'
            return render()

        try:
            rotation = int(rotation)
        except Exception as E:
            errormsg1 = errormsg1 + 'Error: ' + E.__str__()
            rotation = ''
            return render()

        try:
            encrypted_msg = rotate_string(message, int(rotation))
            # raise Exception('simulated error')
        except Exception as E:
            errormsg2 = 'Error encrypting the text: <br>' + E.__str__()
            return render()

        # for debugging purpuses
        # print(message)
        # print(encrypted_msg)

        return render()
        # return form  # '<h1>{}</h1>'.format(encrypted_msg)


@app.route("/")
def index():
    return form.format(rotation=13, errormsg1='', errormsg2='', textmsg='The crow flies at midnight!')

# pending, add the background image


app.run()
