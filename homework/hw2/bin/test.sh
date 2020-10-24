#!/bin/bash

# Array of data-sets
datasetsArr=( NK ZKC ZKW )

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
#methodsArr=( 1 2 )
methodsArr=( 2 )

# Array of items number
itemsCntArr=( 4 10 15 20 )

for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 1 0-499
    done
  done
done