from flask import Flask,render_template,request,flash
from form import ContactForm

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome To Forms"

@app.route('/contact')
def contact(Form):
    if request.method=="POST":
        return "Form Submetted Successfully"
    else:
        return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)