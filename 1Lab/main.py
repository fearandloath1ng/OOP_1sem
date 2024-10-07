import random

class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def get_question(self):
        return self.question

    def get_answers(self):
        return [self.answer1, self.answer2, self.answer3, self.answer4]

    def is_correct(self, answer):
        return answer == self.correct_answer


def main():
    questions = [
        Question("Что такое класс?", "Шаблон для создания объектов", "Объект", "Интерфейс", "Модуль", 1),
        Question("Что такое экземпляр?", "Класс", "Объект класса", "Метод", "Атрибут", 2),
        Question("Что такое наследование?", "Способ создания нового класса на основе существующего", "Способ изменения атрибутов класса", "Способ описания объектов", "Способ взаимодействия классов", 1),
        Question("Что такое инкапсуляция?", "Скрытие данных", "Отображение данных", "Перенос данных", "Передача данных", 1),
        Question("Что такое полиморфизм?", "Способ обработки различных типов", "Способ создания объектов", "Способ разрушения объектов", "Способ ограничения доступа", 1),
        Question("Метод класса обычно принимает в качестве первого параметра:", "self", "cls", "this", "object", 1),
        Question("Какой из этих интерфейсов реализует класс в Python?", "IInterface", "Interface", "abc.ABC", "BaseClass", 3),
        Question("Что такое абстрактный класс?", "Класс, который не может быть инстанцирован", "Класс с единственным объектом", "Класс с фиксированными параметрами", "Класс, содержащий только методы", 1),
        Question("Что такое метод?", "Функция в классе", "Переменная в классе", "Класс в классе", "Свойство класса", 1),
        Question("Какие из этих методов вызываются автоматически при создании объекта?", "__init__", "__str__", "__repr__", "__call__", 1),
        Question("Какой метод отвечает за представление объекта в строковом виде?", "__str__", "__repr__", "__call__", "__init__", 1),
        Question("Как сделать метод статическим?", "@staticmethod", "static", "статический", "метод", 1),
        Question("Для чего нужен метод __del__?", "Для освобождения ресурсов", "Для инициализации", "Для создания объекта", "Для определения класса", 1),
        Question("Что такое интерфейс?", "Список методов, которые должен реализовать класс", "Класс", "Объект", "Файл", 1),
        Question("Python поддерживает множественное наследование. Это правда или ложь?", "Правда", "Ложь", "Не знаю", "Не уверен", 1),
    ]

    students = int(input("Введите количество студентов: "))
    results = []

    for student in range(1, students + 1):
        print(f"\nСтудент {student} отвечает на вопросы:")
        score = 0
        random.shuffle(questions)
        selected_questions = questions[:5]
        for question in selected_questions:
            print("\n" + question.get_question())
            answers = question.get_answers()
            for i, answer in enumerate(answers, 1):
                print(f"{i}. {answer}")
            response = int(input("Выберите номер ответа (1-4): "))
            if question.is_correct(response):
                print("Правильно!")
                score += 1
            else:
                print("Неправильно!")

        results.append((f"Студент {student}", score))

    print("\nРезультаты:")
    for student, score in results:
        print(f"{student}: {score} баллов. Результат: {get_grade(score)}")

def get_grade(score):
    if score > 4:
        return "Отлично"
    elif score > 3:
        return "Хорошо"
    elif score > 2:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

if __name__ == "__main__":
    main()
