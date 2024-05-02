def calculate_bmi(height,weight):
    print("Height=",str(height))
    print("Weight=",str(weight))
    bmi = weight/pow(height,2)
    if bmi < 18.5:
        return "-1"
    elif 18.5 <= bmi <= 25.0:
        return "0"
    else:
        return "1"
    
        

 

def display_main_menu():
    print('Enter some numbers separated by commas') 
    return

def get_user_input():
    result = input()
    return result

print(calculate_bmi(weight=57, height=1.73))


