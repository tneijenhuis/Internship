#!/bin/bash

structures=$(ls . | grep -v [a-z])
run=$1
home=$(pwd)

cd analysis
mkdir analysis_$run
anadir=$home/analysis/analysis_$run
cd ..

for structure in $structures; do
    echo $structure
    cd $structure/$run/structures/it1
    echo structure,HADDOCK-score,atomic-clashes > $anadir/"$structure"_clashes.csv
    pwd
    for complex in *.pdb; do
        score=$(grep $complex file.list | awk '{print $3}')
        clashes=$(/home/abonvin/haddock2.4/tools/contact-chainID $complex 2.5 | wc -l) 
        echo $complex,$score,$clashes >> $anadir/"$structure"_clashes.csv
    done
    cd $home
done
