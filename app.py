import numpy as np
import re
import joblib
import pickle
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
model = joblib.load("loandata.pkl")

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

form_values=[]
@app.route('/QuestionOne', methods=["GET", "POST"])
def QuestionOne():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionOne.html', 
    gender_=[{'gender': 'male'}, {'gender': 'female'}])

@app.route('/QuestionTwo', methods=["GET", "POST"])
def QuestionTwo():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionTwo.html')
    
@app.route('/QuestionThree', methods=["GET", "POST"])
def QuestionThree():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionThree.html', 
    education_=[{'education': 'Master'}, {'education': 'High School'}, {'education': 'Bachelor'}, 
                {'education': 'Associate'}, {'education': 'Doctorate'}])

@app.route('/QuestionFour', methods=["GET", "POST"])
def QuestionFour():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionFour.html')

@app.route('/QuestionFive', methods=["GET", "POST"])
def QuestionFive():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionFive.html', 
    homeownership_=[{"homeownership":"RENT"}, {"homeownership":"OWN"}, {"homeownership":"MORTGAGE"}, 
                       {"homeownership":"OTHER"}])    
    
@app.route('/QuestionSix', methods=["GET", "POST"])
def QuestionSix():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionSix.html') 

@app.route('/QuestionSeven', methods=["GET", "POST"])
def QuestionSeven():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionSeven.html', 
    loandefault_=[{"loandefault":"No"},{"loandefault":"Yes"}])

@app.route('/QuestionEight', methods=["GET", "POST"])
def QuestionEight():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionEight.html') 

@app.route('/QuestionNine', methods=["GET", "POST"])
def QuestionNine():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionNine.html', 
    loanintent_=[{"loanintent":"PERSONAL"}, {"loanintent":"EDUCATION"}, {"loanintent":"MEDICAL"}, 
        {"loanintent":"VENTURE"}, {"loanintent":"HOMEIMPROVEMENT"}, {"loanintent":"DEBTCONSOLIDATION"}])

@app.route('/QuestionTen', methods=["GET", "POST"])
def QuestionTen():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionTen.html')

@app.route('/QuestionEleven', methods=["GET", "POST"])
def QuestionEleven():
    
    form_values.append(list(request.form.values()))
    return render_template('QuestionEleven.html')
    
@app.route('/NextPage', methods=["GET", "POST"])
def NextPage():
    
    form_values.append(list(request.form.values()))
    return render_template("NextPage.html")
    
    
input_dict={'[\'Yes\']': 1, '[\'No\']': 0, '[\'male\']':1, '[\'female\']':0, '[\'Master\']':4, '[\'High School\']':3, 
            '[\'Bachelor\']':1, '[\'Associate\']':0, '[\'Doctorate\']':2, '[\'RENT\']':3, '[\'OWN\']':2, '[\'MORTGAGE\']':0,
           '[\'OTHER\']':1, '[\'PERSONAL\']':4, '[\'EDUCATION\']':1, '[\'MEDICAL\']':3, '[\'VENTURE\']':5, '[\'HOMEIMPROVEMENT\']':2,
            '[\'DEBTCONSOLIDATION\']':0, '[]':0}

					 
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    global form_values
    
    form_values=form_values[-11:]
    print(form_values)
    form_values_=[]
    for i in form_values:
        if bool(re.search(r'\d', i[0])):
            form_values_.append(float(i[0]))       
        else:
            form_values_.append(input_dict.get(str(i)))
        
    
    form_val = np.array(form_values_).reshape(1, -1)
    prediction = model.predict(form_val)
    output = []
    if prediction[0]==1:
        output.append("You will likely get Approved!")
    else:
        output.append("You are unlikely get approved.")
    return render_template(
        'predict.html', prediction_text=str(output[0]))
        
					 
@app.route('/first_page')
def first_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, threaded=True)