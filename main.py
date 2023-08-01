from flask import Flask, render_template, request
import qrcode

app=Flask(__name__, render_template('index.html'))

@app.route('/')
def home():
    return render_template('index.html',"hi" )


if __name__=='__main__':
    app.run(debug=True)
