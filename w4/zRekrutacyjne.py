import csv          # do obróbki plików csv

with open("conferences_data.csv", "r") as file:
    attendantsDirectory = {}
    reader = csv.reader(file, delimiter = ";")
    next(reader)
    for row in reader:
        for conf, email in enumerate(row):
            if not email:
                continue
            try:
                conferences = attendantsDirectory[email]
            except KeyError:
                conferences = set()
                attendantsDirectory[email] = conferences
            conferences.add(conf)


result1 = len([email for email in attendantsDirectory if len(attendantsDirectory[email]) > 1])
print(result1)



def get_company_from_email(email):
    _, rest = email.split("@")          # podłoga (_) to konwencja, nie obchodzi nas wynik
    company, _ = rest.split(".")
    return company

def get_country_from_email(email):
    _, rest = email.split("@")          # podłoga (_) to konwencja, nie obchodzi nas wynik
    _, country = rest.split(".")
    return country

result2 = len([
    email for email in attendantsDirectory
    if get_company_from_email(email) == "wok"
])
print(result2)

result3 = len(set([get_country_from_email(email) for email in attendantsDirectory]))
print(result3)

result3 = len({get_country_from_email(email) for email in attendantsDirectory})     #set comprehension
print(result3)