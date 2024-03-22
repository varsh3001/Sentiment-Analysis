from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

##########################################
@app.route('/')
def index():
  return render_template("home.html")

##########################################
@app.route('/result',methods=['get','post'])
def output():
  if request.method=='POST':
    txt=request.form.get('review')
    if txt:
      data_point=[txt]
      model=joblib.load("model/naive_bayes.pkl")
      prediction=model.predict(data_point)
      if prediction == 'Positive':
        image = 'happy.jpg'
      else:
        image = 'sad.jpg'
      return render_template("output.html", prediction=prediction, image=image)
    else:
      return "No review text Received"
  else:
    return "Error: Only POST requests are allowed"




#run the app
if __name__=='__main__' :
  app.run(debug=True,host='0.0.0.0',port=5000)
  