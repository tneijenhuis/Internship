#!/bin/bash

structures=$(ls . | grep -v [a-z])
run=$1
home=$(pwd)

anadir=$home/analysis/analysis_$run

for structure in $structures; do
    echo $structure
    cd $structure/$run/structures/it1
    echo structure,HADDOCK-score,correlation > $anadir/"$structure"_correlation.csv
    pwd
    for complex in *.pdb; do
        score=$(grep $complex file.list | awk '{print $3}')
        correlation=$(bash /home/tneijen/project/scripts/correlation/calculate_CC_ref.sh $complex | grep "Correlation" | awk '{print $10}' | rev | cut -c2- | rev) 
        echo correlation is $correlation
        echo $complex,$score,$correlation >> $anadir/"$structure"_correlation.csv
    done
    cd $home
done
