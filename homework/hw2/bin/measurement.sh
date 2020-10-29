#!/bin/bash

# Configure result path
resultPath='./../results/measurement'

################################
##  Measure algorithms times  ##
################################

## Array of data-sets
#datasetsArr=( NK )
#
## Array of algorithms
##algorithmsArr=( BruteForce BranchAndBound GreedyRedux DynamicProgramming )
#algorithmsArr=( DynamicProgramming )
#
## Array of items number
#itemsCntArr=( 10 15 )
#
## Prepare result files
#for dataset in "${datasetsArr[@]}"
#do
#  for algorithm in "${algorithmsArr[@]}"
#  do
#    rm "${resultPath}/${dataset}/${algorithm}/time.txt"
#    touch "${resultPath}/${dataset}/${algorithm}/time.txt"
#  done
#done
#
#for dataset in "${datasetsArr[@]}"
#do
#  for algorithm in "${algorithmsArr[@]}"
#  do
#    for n in "${itemsCntArr[@]}"
#    do
#      # Write result into measurement result file
##      echo "Items amount: ${n}" >> "${resultPath}/${dataset}/${algorithm}/time.txt"
#      for measurementRun in {1..3}
#        do
#        for instanceInx in {0..499}
#        do
#          python3 ./../src/main.py "${algorithm}" "${dataset}" "${n}" 0 "${instanceInx}"-"${instanceInx}" 1 | head -n 2 | sed 's/.*in\s//' | sed 's/\sseconds//' | awk -v mr="$measurementRun" 'NR%2{printf "%s %s ",$0,mr;next;}1' >> "${resultPath}/${dataset}/${algorithm}/time.txt"
#        done
#      done
#    done
#  done
#done

#################################
##  Measure greedy heuristics  ##
#################################

### Array of data-sets
#greedyDatasetsArr=( NK ZKC ZKW )
#
### Array of algorithms
#greedyAlgorithmsArr=( Greedy GreedyRedux )
#
### Array of items number
#greedyItemsCntArr=( 4 10 15 20 22)
#
#for dataset in "${greedyDatasetsArr[@]}"
#do
#  for algorithm in "${greedyAlgorithmsArr[@]}"
#  do
#    for n in "${greedyItemsCntArr[@]}"
#    do
#      python3 ./../src/main.py "${algorithm}" "${dataset}" "${n}" 1 0-499 1
#    done
#  done
#done

###############################
##  Measure FPTAS algorithm  ##
###############################

## Array of data-sets
FPTASDatasetsArr=( NK ZKC ZKW )

## Array of items number
greedyItemsCntArr=( 22 )

## FPTAS eps values array
epsArr=( 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 )

for dataset in "${FPTASDatasetsArr[@]}"
do
  rm "${resultPath}/${dataset}/FPTAS/time.txt"
  touch "${resultPath}/${dataset}/FPTAS/time.txt"
done

for dataset in "${FPTASDatasetsArr[@]}"
do
  for n in "${greedyItemsCntArr[@]}"
  do
    for eps in "${epsArr[@]}"
    do
      for measurementRun in {1..3}
      do
        for instanceInx in {0..499}
        do
          python3 ./../src/main.py FPTAS "${dataset}" "${n}" 0 "${instanceInx}"-"${instanceInx}" "${eps}" | head -n 2 | sed 's/.*in\s//' | sed 's/\sseconds//' | awk -v mr="$measurementRun" 'NR%2{printf "%s %s ",$0,mr;next;}1' >> "${resultPath}/${dataset}/FPTAS/time.txt"
        done
      done
    done
  done
done