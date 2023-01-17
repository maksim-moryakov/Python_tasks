# Печать чека. Который растыгивается на всю его ширину.

product = input()
product_price = int(input())
product_weight = int(input())
money = int(input())
price = str(f'{product_price}кг * {product_weight}руб/кг')
itog = product_weight * product_price
money_chek = str(f'{money}руб')
itogo = str(f'{itog}руб')
sdacha = str(f'{money - itog}руб')

print('================Чек================')
print(f'Товар: {product.rjust(28)}')
print(f'Цена: {price.rjust(29)}')
print(f'Итого: {itogo.rjust(28)}')
print(f'Внесено: {money_chek.rjust(26)}')
print(f'Сдача: {sdacha.rjust(28)}')
print('===================================')
