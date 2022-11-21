#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
fam1='wife'
fam2='son'
fam3='daughter'
my_family.append(fam1)
my_family.append(fam2)
my_family.append(fam3)

print(*my_family)

# список списков приблизителного роста членов вашей семьи

fam1=['wife', 160]
fam2=['son', 130]
fam3=['daughter', 110]
fam4=['father', 180]
my_family_height = [
    # ['имя', рост],
    fam1, fam2, fam3, fam4
]
print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ', fam4[1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Общий рост моей семьи - ', fam1[1]+fam2[1]+fam3[1]+fam4[1], 'см')