from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/EFT')
def escape_tarkov():
    return render_template('eft.html')

@app.route('/cooking')
def cooking():
    return render_template('cook.html')

@app.route('/swole')
def fitness():
    return render_template('gym.html')

if __name__ == '__main__':
    app.run(debug=True)
