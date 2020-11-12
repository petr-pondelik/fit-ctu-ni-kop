#!/bin/bash

#############################
##  Test exact algorithms  ##
#############################

## Array of data-sets
#datasetsArr=( NK ZKC ZKW )
#
## Array of algorithms
#methodsArr=( BruteForce BranchAndBound DynamicProgramming )
#
## Array of items number
#itemsCntArr=( 4 10 )
#
#for dataset in "${datasetsArr[@]}"
#do
#  for method in "${methodsArr[@]}"
#  do
#    for n in "${itemsCntArr[@]}"
#    do
#      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-499 0
#    done
#  done
#done

#########################################
##  Test greedy heuristics algorithms  ##
#########################################

# Array of data-sets
datasetsArr=( k5 k60 k120 k200 )

# Array of algorithms
methodsArr=( Greedy )

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

############################
##  Test FPTAS algorithm  ##
############################

## Array of data-sets
#datasetsArr=( NK ZKC ZKW )
#
## Array of algorithms
#methodsArr=( FPTAS )
#
## Array of items number
#itemsCntArr=( 4 10 15 20 22 )
#
#for dataset in "${datasetsArr[@]}"
#do
#  for method in "${methodsArr[@]}"
#  do
#    for n in "${itemsCntArr[@]}"
#    do
#      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-499 0.9
#    done
#  done
#done