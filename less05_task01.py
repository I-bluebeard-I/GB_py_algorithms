"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""


from statistics import mean

company = {}
company_num = int(input('company_num: '))
average_profit = 0

for i in range(company_num):
    name_key = input('company_name: ')
    name_val = []
    for j in range(4):
        name_val.append(int(input(f'profit{j + 1}: ')))
        average_profit += name_val[j]
    company.setdefault(name_key, name_val)

average_profit /= company_num * 4
print(f'{average_profit = }')

less_more = [[], []]
for key, value in company.items():
    if mean(company.get(key)) < average_profit:
        less_more[0].append(key)
    elif mean(company.get(key)) > average_profit:
        less_more[1].append(key)
    else:
        pass

print(company.items())
print(f'The profit is less than the average in next companies: {less_more[0]}')
print(f'The profit is more than the average in next companies: {less_more[1]}')


# company_num: 6
# company_name: qwe
# profit1: 1
# profit2: 1
# profit3: 1
# profit4: 1
# company_name: sdf
# profit1: 2
# profit2: 2
# profit3: 2
# profit4: 2
# company_name: asd
# profit1: 3
# profit2: 3
# profit3: 3
# profit4: 3
# company_name: zxc
# profit1: 3
# profit2: 3
# profit3: 3
# profit4: 3
# company_name: rty
# profit1: 4
# profit2: 4
# profit3: 4
# profit4: 4
# company_name: cvb
# profit1: 5
# profit2: 5
# profit3: 5
# profit4: 5
# average_profit = 3.0
# dict_items([('qwe', [1, 1, 1, 1]), ('sdf', [2, 2, 2, 2]), ('asd', [3, 3, 3, 3]), ('zxc', [3, 3, 3, 3]), ('rty', [4, 4, 4, 4]), ('cvb', [5, 5, 5, 5])])
# The profit is less than the average in next companies: ['qwe', 'sdf']
# The profit is more than the average in next companies: ['rty', 'cvb']
