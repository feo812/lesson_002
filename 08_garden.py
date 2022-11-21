#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
garden_setmeadow_set = garden_set|meadow_set
print(garden_setmeadow_set)

# выведите на консоль те, которые растут и там и там
res=garden_set & meadow_set
res2=garden_set.intersection(meadow_set)

print(res)
print(res2)

# выведите на консоль те, которые растут в саду, но не растут на лугу
res3=garden_set - meadow_set

print(res3)

# выведите на консоль те, которые растут на лугу, но не растут в саду
res4= meadow_set - garden_set

print(res4)


