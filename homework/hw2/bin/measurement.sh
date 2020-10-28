#!/bin/bash

# Configure result path
resultPath='./../results/measurement'

################################
##  Measure algorithms times  ##
################################

# Array of data-sets
datasetsArr=( NK )

# Array of algorithms
algorithmsArr=( BruteForce BranchAndBound GreedyRedux DynamicProgramming )

# Array of items number
itemsCntArr=( 10 )

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
      # Write result into measurement result file
#      echo "Items amount: ${n}" >> "${resultPath}/${dataset}/${algorithm}/time.txt"
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

#################################
##  Measure greedy heuristics  ##
#################################

# TODO: Run algorithms in verbose mode to write results into results/measurement directory

###############################
##  Measure FPTAS algorithm  ##
###############################

# TODO: Run algorithms in verbose mode to write results into results/measurement directory
