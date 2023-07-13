input = input('Enter year: ')
year = int(input)

# if year%4 == 0 and year%100 != 0:
#     print(f'{year} is a leap Year')
# elif year%400 == 0:
#     print(f'{year} is a leap Year')
# else:
#     print(f'{year} is not a leap Year')

if year%4 == 0 :
    if year%100 != 0:
        print(f'{year} is a leap Year')
    elif year%400 == 0:
        print(f'{year} is a leap Year')
    else:
        print(f'{year} is not a leap Year')
else:
    print(f'{year} is not a leap Year')