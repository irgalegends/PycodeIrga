
print('\n-----Celsius Temperature Conversion-----\n')
print('main menu:\n',
      '\nto Fahrenheit (1)',
      '\nto Kelvin     (2)',
      '\nto Reamur     (3)',
      '\nto Rankine    (4)',
      '\nto Delisle    (5)',
      '\nto Newton     (6)\n')

while True:
    menu_option=int(input('$'))
    if menu_option == 1:
        celcius = float(input('temperature(°C):'))
        result  = celcius * 1.8 + 32
        print('celcius to fahrenheit is',result,'°F')
    elif menu_option == 2:
        celcius = float(input('temperature(°C):'))
        result  = celcius + 273.15
        print('celcius to kelvin is',result,'K')
    elif menu_option == 3:
        celcius = float(input('temperature(°C):'))
        result  = celcius * 0.8
        print('celcius to reamur is',result,'°R')
    elif menu_option == 4:
        celcius = float(input('temperature(°C):'))
        result  = (celcius + 273.15) * 1.8
        print('celcius to rankine is',result,'°Rankine')
    elif menu_option == 5:
        celcius = float(input('temperature(°C):'))
        result  = (100 - celcius) * 1.5
        print('celcius to delisle is',result,'°De')
    elif menu_option == 6:
        celcius = float(input('temperature(°C):'))
        result  = celcius * 0.33
        print('celcius to newton is',result,'°N')
    else:
        print('choose according to the available options!!')       
        
        
         