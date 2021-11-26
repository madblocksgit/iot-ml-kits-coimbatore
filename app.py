import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import Flask,render_template,request

data=pd.read_csv('iot_kits.csv')

X=data.iloc[:,1].values
X=X.reshape(-1,1)
Y=data.iloc[:,-1].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
classifier=LogisticRegression()
classifier.fit(X_train,Y_train)

Y_pred=classifier.predict(X_test)

app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/temp',methods=['POST'])
def collectData():
    temp=request.form['temp']
    temp=float(temp)
    out=classifier.predict([[temp]])[0]
    print(out)
    return ('The label dected is %s'%out)

if __name__=="__main__":
    app.run()


