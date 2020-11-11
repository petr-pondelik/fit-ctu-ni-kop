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

# Array of data-sets
datasetsArr=( Greedy )

# Array of algorithms
methodsArr=( BranchAndBound )

# Array of items number
itemsCntArr=( 22 )

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

#########################################
##  Test greedy heuristics algorithms  ##
#########################################

# Array of data-sets
#datasetsArr=( NK ZKC ZKW )
datasetsArr=( Greedy )

# Array of algorithms
#methodsArr=( Greedy GreedyRedux )
methodsArr=( Greedy )

# Array of items number
#itemsCntArr=( 4 10 15 20 22 )
itemsCntArr=( 22 )

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