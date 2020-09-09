# Design a program in Python that read n integer values and then deter-
# mines and outputs whether the sequence entered is sorted in ascending
# order, descending order, or is unordered.
# How many integers do you have? 4
# Enter the 1st integer: 10
# Enter the 2nd integer: 8
# Enter the 3rd integer: 6
# Enter the 4th integer: 4
# Your sequence is sorted in descending order.



n=int(input("How many integers do you have? "))
my_list=[]
for i in range(1, n+1):
    my_numbers=int(input("Enter the integer at position {} : ".format(i)))
    my_list.append(my_numbers)
# print(my_list)
# print(sorted(my_list))
# print(sorted(my_list, reverse=True))
if my_list==sorted(my_list):
    print("Your sequence is sorted in ascending order.")
elif my_list==sorted(my_list, reverse=True):
    print("Your sequence is sorted in descending order.")
else:
    print("Your sequence is not sorted.")
