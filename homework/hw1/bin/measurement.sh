#!/bin/bash

# Configure result path
resultPath='./../res/measurement/'

# Array of data-sets
#datasetsArr=( N Z )
datasetsArr=( N )

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
#methodsArr=( 1 2 )
methodsArr=( 2 )

# Array of items number
itemsCntArr=( 4 )

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
      echo "Items amount: ${n}" >> "${resultPath}${method}${dataset}.txt"
      for measurementRun in {1..3}
        do
        for instanceInx in {0..499}
        do
          python3 ./../src/main.py "${method}" "${dataset}" "${n}" 0 "${instanceInx}"-"${instanceInx}" | head -n 2 | sed 's/.*in\s//' | sed 's/\sseconds//' >> "${resultPath}${method}${dataset}.txt"
        done
      done
    done
  done
done