print('___QUESTION 2_____')

#opening the txt file
with open("fruits.txt", "w")as file:
    print('[THE FRUITS]')
    file.write('Passion_fruit\n')
    file.write('Blueberry\n')
    file.write('Strawberry\n')
    file.write('Apple\n')
    file.write('Cherry\n')

#reaading the txt file
with open("fruits.txt", "r")as file:
    for line in file:
        print(line.strip())
