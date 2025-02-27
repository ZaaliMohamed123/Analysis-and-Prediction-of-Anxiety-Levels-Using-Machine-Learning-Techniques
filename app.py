from flask import Flask,render_template,request,redirect,url_for
from ModelPipelineClass import ModelPipeline
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__,template_folder="templates",static_folder="static", static_url_path="/")

model = ModelPipeline.load('model_pipeline.pkl')

data = {}



@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # Retrieve the values from the form
        gad1 = int(request.form.get('gad1', 0))  # Default to 0 if not found
        gad2 = int(request.form.get('gad2', 0))
        gad3 = int(request.form.get('gad3', 0))
        gad4 = int(request.form.get('gad4', 0))
        gad5 = int(request.form.get('gad5', 0))
        gad6 = int(request.form.get('gad6', 0))
        gad7 = int(request.form.get('gad7', 0))
        gade = request.form.get('gade')
        
        
        data['GAD1'] = gad1
        data['GAD2'] = gad2
        data['GAD3'] = gad3
        data['GAD4'] = gad4
        data['GAD5'] = gad5
        data['GAD6'] = gad6
        data['GAD7'] = gad7
        data['GADE'] = gade
        
        print(data)


        
        return redirect(url_for('swlQuestionnaire'))
    
    
@app.route('/swlQuestionnaire', methods=['GET','POST'])
def swlQuestionnaire():
    if request.method == 'GET':
        return render_template('swlQuestionnaire.html')
    elif request.method == 'POST':
        # Retrieve the values from the form
        swl1 = int(request.form.get('swl1', 0))  # Default to 0 if not found
        swl2 = int(request.form.get('swl2', 0))
        swl3 = int(request.form.get('swl3', 0))
        swl4 = int(request.form.get('swl4', 0))
        swl5 = int(request.form.get('swl5', 0))
        
            
        # Add the SWL data to the existing data
        data['SWL1'] = swl1
        data['SWL2'] = swl2
        data['SWL3'] = swl3
        data['SWL4'] = swl4
        data['SWL5'] = swl5
            
        print(data)
        return redirect(url_for('spinQuestionnaire'))
        
@app.route('/spinQuestionnaire', methods=['GET','POST'])
def spinQuestionnaire():
    if request.method == 'GET':
        return render_template('spinQuestionnaire.html')
    elif request.method == 'POST':
        # Retrieve the values from the SPIN questionnaire
        spin1 = float(request.form.get('spin1', 0))  # Default to 0 if not found
        spin2 = float(request.form.get('spin2', 0))
        spin3 = float(request.form.get('spin3', 0))
        spin4 = float(request.form.get('spin4', 0))
        spin5 = float(request.form.get('spin5', 0))
        spin6 = float(request.form.get('spin6', 0))
        spin7 = float(request.form.get('spin7', 0))
        spin8 = float(request.form.get('spin8', 0))
        spin9 = float(request.form.get('spin9', 0))
        spin10 = float(request.form.get('spin10', 0))
        spin11 = float(request.form.get('spin11', 0))
        spin12 = float(request.form.get('spin12', 0))
        spin13 = float(request.form.get('spin13', 0))
        spin14 = float(request.form.get('spin14', 0))
        spin15 = float(request.form.get('spin15', 0))
        spin16 = float(request.form.get('spin16', 0))
        spin17 = float(request.form.get('spin17', 0))
        
        # Add the SPIN data to the existing data
        data['SPIN1'] = spin1
        data['SPIN2'] = spin2
        data['SPIN3'] = spin3
        data['SPIN4'] = spin4
        data['SPIN5'] = spin5
        data['SPIN6'] = spin6
        data['SPIN7'] = spin7
        data['SPIN8'] = spin8
        data['SPIN9'] = spin9
        data['SPIN10'] = spin10
        data['SPIN11'] = spin11
        data['SPIN12'] = spin12
        data['SPIN13'] = spin13
        data['SPIN14'] = spin14
        data['SPIN15'] = spin15
        data['SPIN16'] = spin16
        data['SPIN17'] = spin17
        
        print(data)
        return redirect(url_for('generalInfo'))
    
@app.route('/generalInfo', methods=['GET','POST'])
def generalInfo():
    if request.method == 'GET':
        return render_template('generalInfo.html')
    elif request.method == 'POST':
        # Retrieve the values from the form
        narcissism = float(request.form.get('narcissism', 0))
        gender = request.form.get('gender')
        age = int(request.form.get('age', 0))
        work = request.form.get('work')
        degree = request.form.get('degree')
        
        # Add the general info data to the existing data
        data['Narcissism'] = narcissism
        data['Gender'] = gender
        data['Age'] = age
        data['Work'] = work
        data['Degree'] = degree
        
        return redirect(url_for('predict_anxiety_level'))
        
@app.route('/predict_anxiety_level', methods=['GET'])
def predict_anxiety_level():
    new_data = pd.DataFrame(data, index=[0])
    print(new_data)
    # Predict the anxiety level
    anxiety_level = model.predict_anxiety_level(new_data)
    
    # Dictionary of recommendations and solutions
    recommendations = {
        "Minimal anxiety": [
            "You seem to be doing well! Keep practicing healthy habits like exercise, relaxation techniques, and a balanced diet to maintain your positive mental well-being.",
            "Consider engaging in activities you enjoy and connecting with loved ones to further enhance your overall well-being."
        ],
        "Mild anxiety": [
            "It's understandable to experience occasional anxiety. Consider implementing stress management techniques such as deep breathing exercises, meditation, or mindfulness to manage your anxiety.",
            "If needed, consider seeking guidance from a mental health professional who can offer personalized strategies and support."
        ],
        "Moderate anxiety": [
            "You might be experiencing significant anxiety. It's important to prioritize self-care and seek support. Try incorporating relaxation techniques, exercise, and a balanced diet into your routine.",
            "Reach out to a mental health professional for personalized guidance and support. There are effective therapies available, such as cognitive-behavioral therapy (CBT), that can help you manage your anxiety."
        ],
        "Severe anxiety": [
            "You're experiencing a high level of anxiety, and it's crucial to prioritize your well-being. Please reach out to a mental health professional or a trusted friend or family member for support.",
            "Consider seeking immediate professional help from a therapist or psychiatrist. There are effective medications and therapies that can provide relief from severe anxiety."
        ]
    }
    
    recommendation = recommendations[anxiety_level][0]
    
    return render_template('predict_anxiety_level.html', anxiety_level=anxiety_level, recommendation=recommendation)
        


if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0'  )