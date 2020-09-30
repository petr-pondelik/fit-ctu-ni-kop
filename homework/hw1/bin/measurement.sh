#!/bin/bash

# Configure result path
resultPath='./../res/measurement/'

# Array of data-sets
datasetsArr=( N Z )

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
methodsArr=( 1 2 )

# Array of items number
itemsCntArr=( 4 10 15 )

# Prepare result files
for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    rm "${resultPath}${method}${dataset}.txt"
    touch "${resultPath}${method}${dataset}.txt"
  done
done

for dataset in "${datasetsArr[@]}"
do
  for method in "${methodsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      # Write result into measurement result file
      echo "${n}" >> "${resultPath}${method}${dataset}.txt"
      python3 ./../src/main.py "${method}" "${dataset}" "${n}" 0 | head -n 1 | sed 's/.*in\s//' | sed 's/\sseconds//' >> "${resultPath}${method}${dataset}.txt"
    done
  done
done