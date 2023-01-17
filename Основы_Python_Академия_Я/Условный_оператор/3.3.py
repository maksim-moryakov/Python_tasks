# Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.
# На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?

spead_Pety = int(input())
spead_Vasya = int(input())
spead_Tolya = int(input())
if spead_Pety > spead_Vasya and spead_Pety > spead_Tolya:
    print('Петя')
elif spead_Vasya > spead_Pety and spead_Vasya > spead_Tolya:
    print('Вася')
elif spead_Tolya > spead_Pety and spead_Tolya > spead_Vasya:
    print('Толя')
    