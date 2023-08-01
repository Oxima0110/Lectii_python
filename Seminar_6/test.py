from puzzle import portfolio

stock = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
price_initial = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
price_current =  {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}


sum_value_initial = portfolio.calculate_portfolio_value(stock, price_initial)
sum_value_current = portfolio.calculate_portfolio_value(stock, price_current)
print(f'Начальная стоимость портфеля акции: {sum_value_initial}')
print(f'Текущаяя стоимость портфеля акции: {sum_value_current}')
rentabilitate = portfolio.calculate_portfolio_return(sum_value_initial, sum_value_current)
print(f'Доходность портфеля: {rentabilitate} %')
max_value = portfolio.get_most_profitable_stock(stock, price_current)
print(f'Наиболее прибыльная акция: {max_value}')



