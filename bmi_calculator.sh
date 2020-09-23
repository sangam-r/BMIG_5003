#!/bin/bash

echo "Enter your first_name"
read first_name
echo "Enter your last_name"
read last_name
echo "enter your weight in lbs"
read weight_lbs

weight_kg=$( echo "$weight_lbs * 0.45" | bc -l) 
echo "Enter your height in inches"
read height_in_inches

height_in_cms=$( echo "$height_in_inches * 2.54" | bc -l) 
height_in_m=$( echo "$height_in_cms/100" | bc -l)

bmi=$( echo "$weight_kg/($height_in_m)^2" | bc -l)

echo Your first name is: $first_name
echo Your last name is: $last_name
echo Your weight in kgs is: $weight_kg
echo Your height in cms is: $height_in_cms
printf "Your bmi is %0.2f\n" $bmi
 
 