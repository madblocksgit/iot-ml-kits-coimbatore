from flask import Flask, request
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/kits',methods=['GET'])
def collectFromIoT():
  humidity=request.args.get('humidity')
  temp=request.args.get('temp')
  print(humidity,temp)
  return('Data Submitted to API')

if __name__=="__main__":
  app.run()
