import json
from flask import Flask, render_template, request
import free

app = Flask(__name__)

class Question:
    q_id=-1
    question=""
    option1=""
    option2=""
    option3=""
    correctOption=-1
    def __init__(self,q_id,question,option1,option2,option3,correctOption):
        self.q_id= q_id
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.correctOption=correctOption
    def get_correct_option(self):        
        if self.correctOption==1:
            return self.option1
        elif self.correctOption==2:
            return self.option2
        elif self.correctOption==3:
            return self.option3

question_list=[]  
for x in range(len(free.q1)):


    q=(free.q1[x])
    q1=Question(q[0],q[1],q[2],q[3],q[4],q[5])
    question_list.append(q1)
 
@app.route("/")
def quiz():
    return render_template("quiz.html",question_list=question_list)
def quiz():
    return render_template("quiz.html",question_list=question_list)

@app.route("/submitquiz",methods=['POST','GET'])
def submit():
    correct_count=0
    incorrect_count=0
    for question in question_list:
        question_id=str(question.q_id)
        selected_option=request.form.get(question_id)
        correct_option=question.get_correct_option()
        if selected_option==correct_option:
            correct_count=correct_count+1
        else:
            incorrect_count+=1
    correct_count=str(correct_count)
    incorrect_count=str(incorrect_count)
    return ('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">'+'<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-indigo.css">'+'<h1 class="w3-theme-l3" style="text-align: center">'+'<br>'+'<br>'+'<br>'+'<p class="w3-theme">'+'Your Correct Answer Score is '+correct_count+'</p>'+'<p class="w3-theme">'+'Your Incorrect Answer Score is '+incorrect_count+'</p>'+'<br>'+'<br>'+'<br>'+'</h1>')
if __name__ == "__main__":
    app.run(debug=True)
