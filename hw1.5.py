students = [
    {"Имя": "Иван", "Фамилия": "Иванов", "Пол": "М", "Опыт": 0, "ДЗ": [6, 4, 8, 5, 2], "Экзамен": 7},
    {"Имя": "Петр", "Фамилия": "Петров", "Пол": "М", "Опыт": 1, "ДЗ": [8, 9, 10, 8, 10], "Экзамен": 9},
    {"Имя": "Семен", "Фамилия": "Семенов", "Пол": "М", "Опыт": 1, "ДЗ": [4, 10, 5, 8, 1], "Экзамен": 5},
    {"Имя": "Снежана", "Фамилия": "Денисова", "Пол": "Ж", "Опыт": 0, "ДЗ": [2, 3, 4, 1, 5], "Экзамен": 3},
    {"Имя": "Мария", "Фамилия": "Кондратьева", "Пол": "Ж", "Опыт": 1, "ДЗ": [5, 10, 7, 5, 10], "Экзамен": 8},
    {"Имя": "Елена", "Фамилия": "Сидорова", "Пол": "Ж", "Опыт": 1, "ДЗ": [4, 6, 9, 10, 5], "Экзамен": 1}

]



def x(stud, sex=None, exp=None): # Средняя по ДЗ

    a = []
    for s in stud:
        if sex is not None and exp is None:
            if s['Пол'] == sex:
                a.append(float(sum(s["ДЗ"])/len(s["ДЗ"])))
        elif exp is not None and sex is None:
            if s['Опыт'] == exp:
                a.append(float(sum(s["ДЗ"])/len(s["ДЗ"])))
        else:
            a.append(float(sum(s["ДЗ"])/len(s["ДЗ"])))

    return float(sum(a)/len(a))

def y(stud, sex=None, exp=None): # Средняя по экзамену
    a = []
    for s in stud:
        if sex is not None and exp is None:
            if s["Пол"] == sex:
                a.append(s["Экзамен"])
        elif exp is not None and sex is None:
            if s["Опыт"] == exp:
                a.append(s["Экзамен"])
        else:
            a.append(s["Экзамен"])
    return float(sum(a)/len(a))

def best_st(stud):
    a = []
    b = []
    for s in stud:
        a.append({'Имя': s['Имя'], 'Фамилия': s['Фамилия'], 'integral_mark': (s['Экзамен'] * 0.4) + (0.6 * x([s]))})
        b.append((s['Экзамен'] * 0.4) + (0.6 * x([s])))
    a = [row for row in a if row['integral_mark'] == max(b)]
    a = a[0]
    print('Лучший студент: {0} {1} с интегральной оценкой: {2}'.format(a['Имя'], a['Фамилия'], a['integral_mark']))


print("Средняя за ДЗ:", x(students), "Средняя за экзамен:", y(students))
print("Средняя за ДЗ у женщин:", x(students, sex='Ж'), "Средняя за экзамен у женщин:", y(students, sex="Ж"))
print("Средняя за ДЗ у мужчин:", x(students, sex='М'), "Средняя за экзамен у мужчин:", y(students, sex="М"))

print("Средняя за ДЗ у студентов с опытом:", x(students, exp=1), "Средняя за экзамен у студентов с опытом:", y(students, exp=1))
print("Средняя за ДЗ у студентов без опыта:", x(students, exp=0), "Средняя за экзамен у студентов без опыта:", y(students, exp=0))
best_st(students)
