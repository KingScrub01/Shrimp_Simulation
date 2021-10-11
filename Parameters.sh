#!/bin/bash
low_num=$1
high_num=$2
step_num=$3
low_vel=$4
high_vel=$5
step_vel=$6
no_chance=$7
high_chance=$8
step_chance=$9
echo " Parameters are: "
echo " Number of shrimp: " $low_num $high_num $step_num
echo " Maximum speed: " $low_vel $high_vel $step_vel
echo " Chance of death: " $no_chance $high_chance $step_chance
for n in `seq $low_num $high_num $step_num`
do
  for v in ` seq $low_vel $high_vel $step_vel `
  do
    for c in `seq $no_chance $high_chance $step_chance`
    do
      echo "Experiment: " $n $v $c
      outfile = "shrimp_N"$n"_v"$v"_C"$c".txt"
      python3 ShrimpSim.py $n $v $c > $outfile
    done
  done
done