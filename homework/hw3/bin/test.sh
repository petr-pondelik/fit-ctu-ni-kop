#!/bin/bash

#########################################
##  Test greedy heuristics algorithms  ##
#########################################

# Array of data-sets
datasetsArr=( k1 k5 k10 k50 k100 k200 k300 )

# Array of algorithms
methodsArr=( Greedy )

# Array of items number
itemsCntArr=( 5 10 15 20 22 25 )

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
