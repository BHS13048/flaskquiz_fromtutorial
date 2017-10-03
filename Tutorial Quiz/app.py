from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

original_questions = {
	'Where is the Taj Mahal?':['Agra','New Delhi','Mumbai','Chennai'],
	'Where is the Great Wall of China?':['China','Beijing','Shanghai','Tianjin'],
	'Where is Petra?':['Ma\'an Governorate','Amman','Zarqa','Jerash'],
	'Where is Machu Picchu?':['Cuzco Region','Lima','Piura','Tacna'],
 	'Where are the Egypt Pyramids?':['Giza','Suez','Luxor','Tanta'],
	'Whrere is the Colosseum?':['Rome','Milan','Bari','Bologna'],
	'Where is Christ the Redeemer?':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)
#function shuffles q - questions is later substituted in order to shuffle the questions.

#home page
@app.route('/')
def home_page():
	print('gets to the index page')
	return render_template('index.html')

@app.route('/quiz')
def quiz():
	print('gets here')
	turns = 15
	if turns == 0:
		return render_template('index.html')
	else:
		turns = turns - 1
		print(turns)
		questions_shuffled = random.choice(list(questions)) #calls for definition, substitutes q for questions.
		print(questions_shuffled)

		for i in questions:
			random.shuffle(questions[i])
			print('gets to this stage')

		#questions.pop(questions_shuffled) #removes the question from the dictionary - currently not working as it also removes the multiple choices
		return render_template('quiz-page.html', q = questions_shuffled, o = questions)

@app.route('/quiz_test')
def mainquiz(): #global is the importing of variables outside the definition
	if request.method == 'GET':
		print('yes')
	else:
		if turns == 0:
			print("Finished")
		else:
			question_answer_no = randrange(0,len(question_list)) #selects a question in random order
			question = question_list[question_answer_no] #sets the question to the random one
			answer = answer_list[question_answer_no] #sets the answer to the one that matches the number of the question in the list, should work as long as the questions are in the matching order as the answers
			question_list.remove(question) 
			answer_list.remove(answer)

		return render_template('main_test.html', q = question)

if __name__ == '__main__':
	app.run(debug=True)