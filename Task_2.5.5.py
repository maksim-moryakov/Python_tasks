# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. 
# Напишите программу, которая определяет номер купе, в котором находится место с заданным номером
place = int(input())
# Для решения задачи надо использовать "Деление с округлением в верх" формула (a + b - 1) / b
room = (place + 4 - 1) // 4 # 4 - это количество мест в купе
print(room)