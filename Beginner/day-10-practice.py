def format_name(f_name, l_name):
    """
    Add a docstring here
    """
    if f_name == "" or l_name == "":
        return "Your inputs are not valid"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("CHI", "wonG"))
print(format_name("", ""))

# Auditorium Exercise
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leap = is_leap(year)
  if leap and month == 2:
    return 29
  return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

format_name

