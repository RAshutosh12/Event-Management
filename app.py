from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('homePage.html')

if __name__ == '__main__':
    app.run(debug=True)