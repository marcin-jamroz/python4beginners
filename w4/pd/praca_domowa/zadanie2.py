# Chcemy napisać sprawdzarkę do testu znajomości stolic europejskich.
# Format listy stolic taki jak w pliku stolice.csv
# Format pytań taki jak w pliku pytania.csv
# Format odpowiedzi taki jak w pliku odpowiedzi.csv

# Napisz funkcję check_homework, która przyjmuje trzy argumenty:
# - capitals_csv to ścieżka do pliku, który zawiera listę stolic europejskich
# - questions_csv to ścieżka pliku csv, który zawiera pytania
# - answers_csv to ścieżka pliku, który zawiera odpowiedzi
# Funkcja zwraca liczbę poprawnych odpowiedzi


import csv

def check_homework(capitals_csv, questions_csv, answers_csv):

    capitalsDictionary = {}
    questionsDictionary = {}
    answers = []

    with open(capitals_csv) as capitals:
        capitalsReader = csv.reader(capitals, delimiter=";")
        next(capitalsReader)
        for row in capitalsReader:
            capitalsDictionary[row[0]] = row[1]

    with open(questions_csv) as questions:
        questionsReader = csv.reader(questions, delimiter=";")
        next(questionsReader)
        for row in questionsReader:
            questionsDictionary[row[0]] = [row[x] for x in range(1,5)]

    with open(answers_csv) as answers:
        answers = [x.strip() for x in answers if x.strip() != "Odpowiedź"]

    correctAnswers = 0
    for enum, question in enumerate(questionsDictionary.items()):
        country = question[0]
        capitals = question[1]
        digitAnswer = 0
        for e, x in enumerate(["A", "B", "C", "D"]):
            if answers[enum] == x:
                digitAnswer = e
                break
        if capitalsDictionary[country] == capitals[digitAnswer]:
            correctAnswers = correctAnswers + 1

    return correctAnswers

c = check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv')
assert check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv') == 5
print(c)