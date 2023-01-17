product, weight, price, money = input(), int(input()), int(input()), int(input())
print('=' * 16 + 'Чек' + '=' * 16)
print('Товар:' + ' ' * (29 - len(product)) + product)
p = f'{price}кг * {weight}руб/кг'
print('Цена:' + ' ' * (30 - len(p)) + p)
i = f'{price * weight}руб'
print('Итого:' + ' ' * (29 - len(i)) + i)
print('Внесено:' + ' ' * (24 - len(str(money))) + str(money) + 'руб')
s = money - price * weight
print('Сдача:' + ' ' * (26 - len(str(s))) + str(s) + 'руб')
print('=' * 35)