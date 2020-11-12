#!/bin/bash

#############################################################
#   Find data for Greedy relative error
#############################################################

# Array of data-sets
datasetsArr=( k200 k300 )

# Array of algorithms
methodsArr=( BranchAndBound )

# Array of items number
itemsCntArr=( 5 10 15 20 22 25 )

for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-499 0
      cp ./../results/measurement/"${dataset}"/"${method}"/"${dataset}"_"${n}"_sol.dat ./../data/"${dataset}"/"${dataset}"_"${n}"_sol.dat
    done
  done
done