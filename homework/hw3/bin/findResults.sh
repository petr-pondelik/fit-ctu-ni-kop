#!/bin/bash

#############################################################
#   Find data for Greedy relative error comparation
#############################################################

# Array of data-sets
datasetsArr=( k5 k60 k120 k180 )

# Array of algorithms
methodsArr=( BranchAndBound )

# Array of items number
itemsCntArr=( 5 10 15 20 22 25 30 )

for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-499 0
    done
  done
done