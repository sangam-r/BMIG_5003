import sys

def height_conversion(my_height):
    return my_height * 2.54

def weight_conversion(my_weight):
    return my_weight * 0.45
def bmi(my_weight, my_height):
    return((my_weight) / (my_height*my_height))

if __name__ == '__main__':
    print("Enter your first name and last name")
    my_name=sys.stdin.readline().split("\n")[0]
    my_name2=my_name.split(" ")
    print("Your first name is %s and last name is %s "% (my_name2[0], my_name2[1]))

    print("Enter your height in inches:")
    my_height=sys.stdin.readline().split("\n")[0]
    print("Your height is %s inches"%(my_height))
    my_height2=my_height.split(" ")
    my_height_inches=float(my_height2[0])
    print("Your height is  %.2f cms" %(height_conversion(my_height_inches)))

    print("Enter your weight in lbs:")
    my_weight=sys.stdin.readline().split("\n")[0]
    print("Your weight is %s pounds"%(my_weight))
    my_weight2=my_weight.split(" ")
    my_weight_lb=float(my_weight2[0])
    print("Your weight is %.2f kilograms"%(weight_conversion(my_weight_lb)))

    print("Your BMI is %.2f kg/m^2"%(bmi((weight_conversion(my_weight_lb)),(height_conversion(my_height_inches/100)))))





