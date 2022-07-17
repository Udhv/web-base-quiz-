
from flask import Flask, render_template, request
import free
import webbrowser


app = Flask(__name__)



class Question:
    q_id=-1
    question=""
    option1=""
    option2=""
    option3=""
    option4=""
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
# choice=int(input("Enter Choice :"))
choice = 1
if choice == 1 :
    for x in range(len(free.q1)):
        q=(free.q1[x])
        q1=Question(q[0],q[1],q[2],q[3],q[4],q[5])
        question_list.append(q1)
else:
    print("Sorry")
    
@app.route("/")
def quiz():
    return render_template("quiz.html",question_list=question_list)

# webbrowser.get("google-brave").open("https://tinyurl.com/yjh94cwb.com")

@app.route("/submitquiz",methods=['POST','GET'])


def submit():
    
    p="Your Score is"
    correct_count=0
    for question in question_list:
        question_id=str(question.q_id)
        selected_option=request.form[question_id]
        correct_option=question.get_correct_option()
        if selected_option==correct_option:
            correct_count=correct_count+1
    correct_count=str(correct_count) 
    return ('<h1 style="text-align:center; background-color:red;">'+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"</h1>"+'<h1 style="text-align:center; background-color:yellow;">'+p+correct_count+'</h1>'+'<h1 style="text-align:center; background-color:red;">'+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"<br>"+"</h1>")

    

if __name__ == "__main__":
    app.run(debug=True)
