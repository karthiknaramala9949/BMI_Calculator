from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bmi_calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        # Calculate BMI
        bmi = weight / float(height ** 2)
        
        # Classify BMI
        if bmi < 18.5:
            classification = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            classification = 'Normal weight'
        elif 25 <= bmi < 29.9:
            classification = 'Overweight'
        else:
            classification = 'Obese'

        return render_template('bmi_result.html', bmi=bmi, classification=classification)

if __name__ == '__main__':
    app.run(debug=True)
