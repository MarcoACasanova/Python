import datetime

# Criar objeto datetime para 4 de novembro de 2020, 14:53:00
dt = datetime.datetime(2020, 11, 4, 14, 53, 0)

# Formatar a data e hora com as diretivas apropriadas
formatted_date1 = dt.strftime('%Y/%m/%d %H:%M:%S')
formatted_date2 = dt.strftime('%y/%B/%d %I:%M:%S %p')
formatted_date3 = dt.strftime('%a, %Y %b %d')
formatted_date4 = dt.strftime('%A, %Y %B %d')
formatted_date5 = dt.strftime('Weekday: %w')
formatted_date6 = dt.strftime('Day of the year: %j')
formatted_date7 = dt.strftime('Week number of the year: %U')

# Exibir os resultados
print(formatted_date1)
print(formatted_date2)
print(formatted_date3)
print(formatted_date4)
print(formatted_date5)
print(formatted_date6)
print(formatted_date7)
