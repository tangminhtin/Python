height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))
bmi = int(weight / height ** 2)
mess = ''
if bmi < 18.5:
    mess = 'underweight'
elif bmi < 25:
    mess = 'normal weight'
elif bmi < 30:
    mess = 'overweight'
elif bmi < 35:
    mess = 'obese'
else:
    mess = 'clinically obese'

print(f'Your BMI is {bmi}, you are {mess}.')
