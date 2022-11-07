per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую вы планируете положить под проценты: "))
deposit = []
for value in per_cent.values():
    result = int (money / 100 * value)
    deposit.append(result)
print("Нокопленные средства за год вклада в каждом из банков:", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))