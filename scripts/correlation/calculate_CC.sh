#!/bin/bash

shopt -s expand_aliases
source /home/sbgrid/programs/sbgrid.shrc
searches=$2

pdb_file=$1 
struct=${pdb_file:0:4}
 #echo $struct
resolution=$(cat ~/project/data/em-maps/"$struct".info | awk '{print $1}')
 #echo $resolution
map=~/project/data/em-maps/"$struct".map
 #echo $map	


chimera --nogui --script "/home/tneijen/project/scripts/correlation/CCcalculate.py $pdb_file $map $resolution $searches" << do
do
  

