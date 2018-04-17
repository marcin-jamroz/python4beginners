result = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

for i, j in result.copy().items():
    if i % 2 != 0:
       del result[i]
       result[j] = i
    else:
        del result[i] 

assert "Poniedziałek" in result