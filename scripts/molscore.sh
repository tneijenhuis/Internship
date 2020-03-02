#!/bin/bash
shopt -s expand_aliases
source /home/sbgrid/programs/sbgrid.shrc

/home/sbgrid/programs/x86_64-linux/phenix/1.14-3260/bin.capsules/molprobity.molprobity $1
rm -f molprobity_coot.py
rm -f molprobity_probe.txt
grep Clashscore molprobity.out | awk '{print $3}'
grep Ramachandran molprobity.out | awk '{print $4}'
grep Rotamer molprobity.out | '{print $4}'
grep MolProbity molprobity.out | awk '{print $4}' 
rm -f molprobity.out
 
