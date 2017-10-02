from flask import Flask, render_template
from random import randrange

app = Flask(__name__)

#variables and flags to start with
question_no = 0
correct_answers = 0
incorrect_answers = 0
turns = 15
question = ""
flag = True
age_flag=False

#question list
question_list = [' Which country features a maple leaf on it’s flag?', 'Who wrote the Harry Potter series?', 'What is the 2nd most disliked video on YouTube?', 'What sport is Sachin Tendulkar famous for?', 'What sport is Valerie Adams famous for?', 'What is the most important component for a time machine, featured in Back to the Future?', 'Which country takes in the most refugees?', 'What is the second largest secondary school in New Zealand?', 'What is the international language used all over the world?', 'Which well known director is used for using extraordinary amounts of explosions in his films?', 'What is the highest rated movie on iMDB?','What is one of the best TV series that featured Aaron Paul and was producted by AMC?', 'What is the name of the company that designed the iPhone?', 'Who is Winnie the Poohs gloomy donkey friend?', 'What is the name of the famous character from the late 1980s notorious for making the sound "noot"?', 'What is 1 + 3?', 'What do you call a group of fish?', 'How many years are there in a century?']

#answer list
answer_list = ['Canada', 'JK Rowling', 'Infinite Warfare Reveal Trailer', 'Cricket', 'Shot-put', 'Flux Capacitor', 'Turkey', 'Burnside High School', 'English', 'Michael Bay', 'The Shawshank Redemption', 'Breaking Bad', 'Apple', 'Eeyore', 'Pingu', '4', 'A school', '100']

#definitions
''' def space(): #unnecessary but did it for fun :)
    print("")
    
def agegroup(_age):
    if _age < 10 or _age == 10:
        return 1
    else:
        return 2
        
def turns(_agegroup):
    if _agegroup ==1:
        return 10
    else:
        if _agegroup ==2:
            return 15

def realage():
    try:
        global age
        float(age)
        age = int(age)
        if age < 101 and age > 0: #makes sure that the number is valid and between 101 and 0
            global age_flag
            age_flag=True
        else:
            return print('Not a number between 101 and 0')
    except ValueError:
        return print('Not a number between 101 and 0') '''

@app.route('/')
def homepage(): #global is the importing of variables outside the definition

    question_answer_no = randrange(0,len(question_list)) #selects a question in random order
    question = question_list[question_answer_no] #sets the question to the random one
    answer = answer_list[question_answer_no] #sets the answer to the one that matches the number of the question in the list, should work as long as the questions are in the matching order as the answers
    #removes the question and answer chosen from the list so the user does not have it repeated.
    question_list.remove(question) 
    answer_list.remove(answer)    
    return render_template('main_test.html', q = question)

@app.route('/quiz_test')
def mainquiz(): #global is the importing of variables outside the definition
    turns = turns - 1   
    if turns == 0:
        print("Finished")
    else:
        question_answer_no = randrange(0,len(question_list)) #selects a question in random order
        question = question_list[question_answer_no] #sets the question to the random one
        answer = answer_list[question_answer_no] #sets the answer to the one that matches the number of the question in the list, should work as long as the questions are in the matching order as the answers
        question_list.remove(question) 
        answer_list.remove(answer)
 
        return render_template('main_test.html', q = question)

''' #user friendliness :)
print("Welcome to my General Knowledge Quiz")
(space())
name = input("What is your name?")
print("Hello", name)
(space())

#start of program
while age_flag==False:
    age = input("What is your age?")
    (space())
    (realage()) #calls for function that decides if the user has entered a valid age
    
agegroup = (agegroup(age)) '''


''' while flag ==True: #program ends when false
    if turns == 1:
        flag = False
    else:
        turns = turns -1 #subtracts when question is answered
    (questionchoosing()) #calls for definition for question and answer
    question_no = question_no + 1
    print("Question ",question_no," of ",totalturns)
    (space())
    
    user_answer = input(question)

    if user_answer == answer.lower() or user_answer == answer: #program accepts both capital and non-capital letters
        correct_answers = correct_answers +1 #adds correct answers
        print('Correct')
    else:
        incorrect_answers = incorrect_answers +1 #adds incorrect answers
        print('Incorrect')
    (space())

#out of the loop

print('The number of incorrect answers was', incorrect_answers)
print('The number of correct answers was', correct_answers)
(space())
try:
    print("You received a percentage of ",(correct_answers / totalturns * 100),"%")
    if (correct_answers / totalturns * 100) == 100: #calculates the percentage correct
        print("Congratulations!!!")    
except ZeroDivisionError: #removes the error of anything divided by 0 breaking the program
    print("You received a percentage of 0%")
    print("Were you even trying?!?") '''

if __name__ == '__main__':
 app.run(debug=True)