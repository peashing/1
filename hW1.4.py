documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def p():
    print('Введите номер документа...')
    number = input()
    for x in documents:
        if x['number'] == number:
            print('ФИО владельца:', x.get('name'))


def l():
    for x in documents:
        print('{0} "{1}" "{2}"'.format(x['type'], x['number'], x['name']))

def s():
    print('Введите номер документа...')
    number = input()
    for x in directories.keys():
        if number in directories[x]:
            print('Номер полки на которой лежит документ:', x)

def a():
    print('Добавляем документ:')
    print('Введите номер документа...')
    number = input()
    print('Введите тип документа...')
    type = input()
    print('Введите ФИО владельца документа...')
    holder = input()
    print('Введите номер полки для документа(1-3)...')
    polka = input()
    documents.append({'type': type, 'number': number, 'name': holder})
    if int(polka) > 3 or int(polka) < 1:
        print('Нет такой полки!!!')
    else:
        directories[polka].append(number)


l()

a()

l()

for x in directories.items():
    print(x)

print('Done')
input()
