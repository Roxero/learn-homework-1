"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
	"Привет": "Добрый день",
	"Как дела?": "Норм",
	"Что делаешь?": "Программирую",
	"На чем?": "На python",
	"Сложно?": "Пока нет"
}

def ask_user(answers_dict):
	while True:
		question = input('Ваш вопрос: ')
		if question == 'Пока':
			print('Ну, пока')
			break
<<<<<<< HEAD
		answer = questions_and_answers.get(question, 'Не знаю. Другой вопрос, пожалуйста')
		print(answer)
		
=======
		if question.strip() in questions_and_answers:
			print(questions_and_answers[question])
		else:
			print('Не знаю. Другой вопрос, пожалуйста')

>>>>>>> 7b1c9e40ed51e4fd47ff6c4d3f06ec703dbf72e3
if __name__ == "__main__":
    ask_user(questions_and_answers)
