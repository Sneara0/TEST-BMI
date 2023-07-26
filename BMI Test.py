weight=float(input("Enter yur weight in kg:"))

height=float(input("Enter yur weight in meters:"))

BMI=weight/height**2
if BMI<18.5:
    print("under weight")
elif BMI<25:
    print("Healthy weight")
else:
    print("over weight")

