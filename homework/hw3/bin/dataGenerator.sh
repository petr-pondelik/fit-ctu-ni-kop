#!/bin/bash

#############################################################
#   Generate data for Branch & Bound dependency
#############################################################

# Array of items cnt
itemsCntArr=( 5 10 15 20 22 25 30 )

# Array of knapsack generator m parameters
mArr=( 0.05 0.1 0.2 0.3 )

# Array of result files names
namesArr=( m005 m01 m02 m03 )

for n in "${itemsCntArr[@]}"
do
  for mInx in "${!mArr[@]}"
  do
    ./../kg2/gen/kg2 -n "${n}" -N 500 -m ${mArr[mInx]} -W 300 -C 1500 -c corr > ./../data/"${namesArr[mInx]}"/"${namesArr[mInx]}"_"${n}"_inst.dat
  done
done

#############################################################
#   Generate data for Greedy dependency
#############################################################

# Array of items cnt
itemsCntArr=( 5 10 15 20 22 25 30 )

# Array of knapsack generator granularity exponents
mArr=( 5 60 120 180 )

# Array of result files names
namesArr=( k5 k60 k120 k180 )

for n in "${itemsCntArr[@]}"
do
  for mInx in "${!mArr[@]}"
  do
    ./../kg2/gen/kg2 -n "${n}" -N 500 -m ${mArr[mInx]} -W 300 -C 1500 -c corr > ./../data/"${namesArr[mInx]}"/"${namesArr[mInx]}"_"${n}"_inst.dat
  done
done