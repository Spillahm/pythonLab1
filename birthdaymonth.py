from datetime import datetime

today_datetime = datetime.now()
print(today_datetime)
today_month_number = today_datetime.month
print(today_month_number)

current_month_text = today_datetime.strftime('%B')
print(current_month_text)

name = input('Please enter your name:')
birthday_month = input('Enter the month with your birthday: ')

print(f'Hello {name} !')

letters_in_name = len(name)

print(f'Your name{name} has {letters_in_name} letters. ')

if birthday_month.lower() == 'january':
    print('happy birthday month!')

else:
    print('your bithday is not this month!')