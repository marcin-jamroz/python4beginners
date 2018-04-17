# Chcemy napisać kod, który dla danego pliku z listą stolic wygeneruje number_of_sets zestawów pytań po number_of_questions_per_set pytań
# - Format listy stolic taki jak w stolice.csv
# - Format oczekiwanego pojedynczego zestawu pytań taki jak w pliku pytania.csv - prosimy pamiętać o nagłówkach
# - Każdy zestaw powinien znaleźć się w osobnym pliku - pierwszy w zestaw1.csv, drugi w zestaw2.csv itd (nie ma czegoś takiego jak zestaw 0)
# - pliki zestaw1.csv, zestaw2.csv itd. powinny się stworzyć w folderze z rozwiązaniem zadania (tzn. przy otwieraniu pliku nie podawać żadnej ścieżki, tylko samą nazwę pliku)
#
# Dodatkowe założenia:
# Pytanie o jeden kraj nie może wystąpić więcej niż raz (biorąc pod uwagę wszystkie zestawy)
# W przypadku, gdy ktoś poda nam dane, dla których musielibyśmy wygenerować więcej niż 48 pytań (tyle mamy stolic w pliku stolice.csv) - rzućmy ValueError
# Poprawna odpowiedź powinna znajdować się w losowej kolumnie - tzn. losowo powinna być odpowiedzią A, B, C lub D
# Do losowania należy skorzystać z modułu random https://docs.python.org/3/library/random.html

import csv
import random


def create_sets_of_question(capitals_csv, number_of_sets,
                            number_of_questions_per_set):
    if number_of_sets * number_of_questions_per_set > 48:
        raise ValueError

    countries = []
    capitals = []
    countries_capitals = {}

    with open(capitals_csv) as capitals_tmp:
        capitalsReader = csv.reader(capitals_tmp, delimiter=";")
        next(capitalsReader)
        for row in capitalsReader:
            countries_capitals[row[0]] = row[1]
            countries.append(row[0])
            capitals.append(row[1])
    for x in range(1, number_of_sets + 1):
        with open("zestaw" + str(x) + ".csv", "w") as csv_file:
            csvWriter = csv.writer(csv_file, delimiter=";")
            headline = ["Państwo", "A", "B", "C", "D"]
            csvWriter.writerow(headline)

            for i in range(number_of_questions_per_set):
                country = random.choice(countries)
                countries.remove(country)

                tmp = [countries_capitals[country]]
                i = 0
                while i < 3:
                    choice = random.choice(capitals)
                    if choice not in tmp:
                        tmp.append(choice)
                        i = i + 1

                random.shuffle(tmp)
                csvWriter.writerow([country].__add__(tmp))


create_sets_of_question('stolice.csv', 1, 8)

with open('zestaw1.csv') as zestaw1:
    reader = csv.reader(zestaw1, delimiter=';')
    lines_count = 0
    for row in reader:
        print(row)
        assert len(
            row) == 5  # 5 kolumn - Państwo + propozycje odpowiedzi A, B, C, D
        lines_count += 1
    assert lines_count == 9  # 8 pytan + naglowek

try:
    create_sets_of_question('stolice.csv', 5, 10)
except ValueError:
    print('Błąd wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')
