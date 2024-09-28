from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

def assess_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

@app.route('/check_password/<password>', methods=['GET'])
def check_password(password):
    strength = assess_password_strength(password)
    return {"password": password, "strength": strength}

if __name__ == '__main__':
    app.run(debug=True)