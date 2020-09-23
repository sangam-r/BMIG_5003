#!/bin/bash

echo Please enter how many integers ?
read numbers
counter=0
my_array=()
while [ $counter -lt $numbers ]; do
    let counter+=1
    echo please enter $counter position integers
    read num
    my_array+=("$num")
done
clear

echo "My list is: " ${my_array[*]} 
sorted=$( echo ${my_array[*]} | tr " " "\n" | sort | tr "\n" " ") 
# printf "\n"
echo "Sorted in ascending order is:"${sorted[*]}

sorted_reverse=$( echo ${my_array[*]} | tr " " "\n" | sort -r | tr "\n" " ")
echo "Sorted in descending order is:" ${sorted_reverse[*]}

if [[ ${my_array[*]} == ${sorted[*]} ]]; then 
	echo "The inputs are in ascending order"

elif [[ ${my_array[*]} == ${sorted_reverse[*]} ]]; then
	echo "The list is in descending order"
else
	echo "The list is unordered"
fi
