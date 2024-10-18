money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_counter = 0

while True:
    budget = money_capital + salary
    if budget < spend: break
    money_capital = budget - spend
    spend *= 1.05
    month_counter += 1
print("Количество месяцев, которое можно протянуть без долгов:", month_counter)
