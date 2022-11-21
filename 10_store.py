#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость:', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

tables_cost = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print('Стол -', store[goods['Стол']][1]['quantity'], 'шт, стоимость: ', tables_cost, 'руб')

table_code = goods['Стол']
tables_item = store[table_code][0]
table_quantity = tables_item['quantity']
table_price = tables_item['price']
tables_cost2 = table_quantity * table_price
print('Cmol', 'в количестве: ', table_quantity, 'шт, стоимостью: ', tables_cost2, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofas_cost = sofa_quantity * sofa_price
print('Sofa', 'в количестве: ', sofa_quantity, 'шт, стоимостью: ', sofas_cost, 'руб')

chear_code = goods['Стул']
chear_item = store[chear_code][0]
chear_item2 = store[chear_code][1]
chear_item3 = store[chear_code][2]
chear_quantity = chear_item['quantity']
chear_quantity2 = chear_item2['quantity']
chear_quantity3 = chear_item3['quantity']
chear_price = chear_item['price']
chear_price2 = chear_item2['price']
chear_price3 = chear_item3['price']
chears_cost = chear_quantity * chear_price
chears_cost2 = chear_quantity2 * chear_price2
chears_cost3 = chear_quantity3 * chear_price3

print('Стул в количестве: ', chear_quantity, 'шт, стоимостью: ', chear_price, 'руб')
print('Стул2 в количестве: ', chear_quantity2, 'шт, стоимостью: ', chear_price2, 'руб')
print('Стул3 в количестве: ', chear_quantity3, 'шт, стоимостью: ', chear_price3, 'руб')
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






