money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
MONTHS = 0
BUDGET = salary+money_capital
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend <= BUDGET:
    MONTHS += 1
    BUDGET = BUDGET - spend + salary
    spend = spend + spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", MONTHS)
