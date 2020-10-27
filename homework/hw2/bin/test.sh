#!/bin/bash

# Array of data-sets
datasetsArr=( NK ZKC ZKW )

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
#methodsArr=( BruteForce )
#methodsArr=( BranchAndBound )
methodsArr=( DynamicProgramming )

# Array of items number
itemsCntArr=( 10 )

for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-2
    done
  done
done