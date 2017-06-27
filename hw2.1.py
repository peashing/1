
def readreciept(file):
    dishes = {}
    with open(file, 'rt', encoding='cp1251') as f:
        for line in f:
            dish = line.strip()
            dishes[dish] = []
            #print(dish)
            count_ingridients = f.readline().strip()
            #print(count_ingridients)
            for i in range(int(count_ingridients)):
                ing_list = f.readline().split('|')
                ing_list[1] = int(ing_list[1])
                ing_list = [row for row in ing_list if row != '\n']
                ing_list = dict(zip(['ingridient_name', 'quantity', 'measure'], ing_list))
                dishes[dish].append(ing_list)
                #print(ing_list)
            f.readline()
    return dishes

cook_book = readreciept('C:/Python36/file.txt')

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))
def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
