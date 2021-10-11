A simulation of a Brine population for COMP1005
Note: Not all the features are working properly,
and the program has been left essentially as it was submitted

## Contents

README - Readme file for shrimp simulation
Egg.png - Reference image file for egg state in Shrimp class
Hatchling.png - Reference image file for hatchling state in Shrimp class
Juvenile.png - Reference image file for juvenile state in Shrimp class
Adult_Male.png - Reference image file for a male adult in Shrimp class
Adult_Female.png - Reference image file for a female adult in Shrimp class
Dead.png - Reference image file for dead state in Shrimp class
Shrimp_Class.py - Program that writes a class for shrimp and then simulates
a colony's lifecycle

## Dependencies

Modules used - random - pygame - sys - time

## Version Information

29/10/2019 - Runnable version with minor bugs, parameter sweeps not working
30/10/2019 - Final version for submission, minor bugs still need to be
addressed. Though they don't influence output significantly

## Run Guide

- To run make sure all files and dependencies are accounted for.
- To run with parameter sweep enter 'sh Parameters.sh <lowest initial shrimp>
  <highest initial shrimp> <step size between runs> <lowest velocity>
  <highest velocity> <step size between velocities> <lowest chance of death>
  <highest chance of death> <step between chances>'
  So the command should take 9 parameters for the sweep.
- See output files for information for sweep. See user guide for more info.
