#!/bin/bash

# Configure result path
resultPath='./../results/measurement'

# Array of items number
itemsCntArr=( 5 10 15 20 22 25 )

###################################################
##      Measure Branch & Bound times
###################################################

# Array of data-sets
datasetsArr=( m005 m01 m02 m03 )

# Array of algorithms
algorithmsArr=( BranchAndBound )

# Prepare result files
for dataset in "${datasetsArr[@]}"
do
  for algorithm in "${algorithmsArr[@]}"
  do
    rm "${resultPath}/${algorithm}/time.txt"
    touch "${resultPath}/${algorithm}/time.txt"
  done
done

for dataset in "${datasetsArr[@]}"
do
  for algorithm in "${algorithmsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      for measurementRun in {1..3}
        do
        for instanceInx in {0..499}
        do
          python3 ./../src/main.py "${algorithm}" "${dataset}" "${n}" 0 "${instanceInx}"-"${instanceInx}" 1 | head -n 2 | sed 's/.*in\s//' | sed 's/\sseconds//' | awk -v mr="$measurementRun" 'NR%2{printf "%s %s ",$0,mr;next;}1' >> "${resultPath}/${dataset}/${algorithm}/time.txt"
        done
      done
    done
  done
done

###################################################
##      Measure Dynamic Programming times
###################################################

# Array of data-sets
datasetsArr=( C100 C500 C1500 C4000 )

# Array of algorithms
algorithmsArr=( DynamicProgramming )

# Prepare result files
for dataset in "${datasetsArr[@]}"
do
  for algorithm in "${algorithmsArr[@]}"
  do
    rm "${resultPath}/${dataset}/${algorithm}/time.txt"
    touch "${resultPath}/${dataset}/${algorithm}/time.txt"
  done
done

for dataset in "${datasetsArr[@]}"
do
  for algorithm in "${algorithmsArr[@]}"
  do
    for n in "${itemsCntArr[@]}"
    do
      for measurementRun in {1..3}
        do
          for instanceInx in {0..499}
          do
            python3 ./../src/main.py "${algorithm}" "${dataset}" "${n}" 0 "${instanceInx}"-"${instanceInx}" 1 | head -n 2 | sed 's/.*in\s//' | sed 's/\sseconds//' | awk -v mr="$measurementRun" 'NR%2{printf "%s %s ",$0,mr;next;}1' >> "${resultPath}/${dataset}/${algorithm}/time.txt"
          done
        done
      done
    done
  done
done