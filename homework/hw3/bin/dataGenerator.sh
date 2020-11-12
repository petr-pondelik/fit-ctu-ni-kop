#!/bin/bash

# Array of items cnt
itemsCntArr=( 5 10 15 20 22 25 )

#############################################################
#   Generate data for Branch & Bound dependency
#############################################################

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

# Array of knapsack generator granularity exponents
kArr=( 1 5 10 50 100 200 300 )

# Array of result files names
kNamesArr=( k1 k5 k10 k50 k100 k200 k300 )

for n in "${itemsCntArr[@]}"
do
  for kInx in "${!kArr[@]}"
  do
    ./../kg2/gen/kg2 -n "${n}" -m 0.2 -N 500 -W 300 -w light -C 1500 -k ${kArr[kInx]} > ./../data/"${kNamesArr[kInx]}"/"${kNamesArr[kInx]}"_"${n}"_inst.dat
  done
done

#############################################################
#   Generate data for Dynamic Programming dependency
#############################################################

# Array of knapsack items maximal prices
CArr=( 100 500 1500 4000 )

# Array of result files names
CNamesArr=( C100 C500 C1500 C4000 )

for n in "${itemsCntArr[@]}"
do
  for CInx in "${!CArr[@]}"
  do
    ./../kg2/gen/kg2 -n "${n}" -N 500 -W 300 -C ${CArr[CInx]} -c strong > ./../data/"${CNamesArr[CInx]}"/"${CNamesArr[CInx]}"_"${n}"_inst.dat
  done
done