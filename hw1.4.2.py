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
    tip = input()
    print('Введите ФИО владельца документа...')
    holder = input()
    print('Введите номер полки для документа(1-3)...')
    shelf = input()
    documents.append({'type': tip, 'number': number, 'name': holder})
    if int(shelf) > 3 or int(shelf) < 1:
        print('Нет такой полки!!!')
    else:
        directories[shelf].append(number)
        for d in directories.items():
          print(d)


while True:
  print("Введите номер команды")
  command = input()
  if command == 'p':
    p()
  elif command == 'l':
    l()
  elif command == 's':
    s()
  elif command == 'a':
    a()
  else:
    print('Команда не распознана! Выходим!')
    break
