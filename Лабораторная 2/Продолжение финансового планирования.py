salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
MONEY_CAPITAL = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(0, months):
    MONEY_CAPITAL = MONEY_CAPITAL + spend - salary
    spend = spend + spend * increase
MONEY_CAPITAL = int(MONEY_CAPITAL)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", MONEY_CAPITAL)
