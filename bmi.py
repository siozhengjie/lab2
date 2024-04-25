def calculate_bmi(height,weight):
    print("Height="+ str(height))
    print("Weight="+str(weight))
    bmi = weight/pow(height,2)
    return bmi

print(calculate_bmi(weight=57, height=1.73))

