#########################################################################################################123
# 1 Решение

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}     # создаем словарь со списком банков и процентных ставок

money = int(input("введите сумму: "))                             # создаем переменную для ввода размера вклада

deposit = []                                                      # создаем пустой список куда будем сохранять информацию с накопленными средствами в каждом из банков

deposit.append(int(per_cent.get("ТКБ") * money / 100))          # сохраняем информацию с накопленными
deposit.append(int(per_cent.get("СКБ") * money / 100))          # средствами по банку,
deposit.append(int(per_cent.get("ВТБ") * money / 100))          # с приведением к целому числу, как указано в примере-условии
deposit.append(int(per_cent.get("СБЕР") * money / 100))         #

print("Накопленные средства -", deposit)

max_deposit = max(deposit)                                        # создаем переменную куда, с помошью метода "max" сохраняем максимальное значение накопленных
print("Максимальная сумма, которую вы можете заработать — ", str(max_deposit))

###########################################################################################################
# 2 решение, с помошью циклов
deposit_cycle = []

for key in per_cent:                                              # создаем цикл "for", с помошью которого, проделываем аналогичную операцию, что и в решении 1.     
    deposit_cycle.append(int(per_cent[key] * money / 100))      # если бы банков в условии было несколько сотен, то первое решение было бы не самым верным))  

print("Накопленные средства -", deposit_cycle)

max_deposit_cycle = max(deposit_cycle)

print("Максимальная сумма, которую вы можете заработать — ", str(max_deposit_cycle))

############################################################################################################
# 3 решение(lambda)

deposit_lambda = list(map(lambda deposit_percent: round(deposit_percent * money / 100), per_cent.values()))

print('Накопленные средства -', deposit_lambda)  

print('Максимальная сумма, которую вы можете заработать —', max(deposit_lambda))                                              

