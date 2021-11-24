from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def homePage():
  return render_template('log.html')

@app.route('/temp',methods=['POST','GET'])
def collectData():
  t=request.form['temp'] # from - form
  print (t)
  return (t)

if __name__=="__main__":
  app.run()
