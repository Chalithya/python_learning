length = float(input("Enter the length: "))

type = input('''
    Milimeters : mm
    Centimeters : c
    Meters : m
    Kilometers : km
    Enter the relevant symbol for your input unit : ''')
values = []
if type.upper()=='MM':
    values.append(length)
    values.append(length/10)
    values.append(length/10**3)
    values.append(length/10**6)
    type =' mm'

elif type.upper()== 'C':
    values.append(length*10)
    values.append(length)
    values.append(length/10**2)
    values.append(length/10**5)
    type = ' cm'

elif type.upper()== 'M':
    values.append(length*10**3)
    values.append(length*10**2)
    values.append(length)
    values.append(length/10**3)
    type = ' m'

elif type.upper()== 'KM':
    values.append(length*10**6)
    values.append(length*10**5)
    values.append(length*10**3)
    values.append(length)
    type = ' km'

else :
    print("Type mismatch")


answerType = input('''
    Milimeters : mm
    Centimeters : c
    Meters : m
    Kilometers : km
    Enter your output option: ''')

if answerType.upper()=='MM':
    print(f'{str(length)+type} = {str(values[0])} mm')

elif answerType.upper()== 'C':
    print(f'{str(length)+type} = {str(values[1])} cm')
   
elif answerType.upper()== 'M':
    print(f'{str(length)+type} = {str(values[2])} m')

elif answerType.upper()== 'KM':
    print(f'{str(length)+type} = {str(values[3])} km')

else :
    print("Type mismatch")


# print(values[0])
# print(values[1])
# print(values[2])
# print(values[3])
