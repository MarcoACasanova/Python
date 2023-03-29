def is_year_leap(year):
    if year % 400 != 0 and year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 4 == 0 and year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
	days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month == 2 and is_year_leap(year):
		return 29
	elif month == 2:
		return 28
	else:
		return days_per_month[month - 1]

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)
    day_of_year += day

    return day_of_year

print(day_of_year(1992, 11, 11))