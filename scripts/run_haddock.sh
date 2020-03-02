#!/bin/bash

shopt -s expand_aliases
source /home/abonvin/haddock2.4/haddock_configure.sh

# get name of the complex to be refined
complex=`pwd | rev | cut -d '/' -f 2 | rev`

# chech weither there is a density map supplied 
if grep -q "CRYO-EM_FILE=" "./data/run.param"; then
    resolution=`cat /home/tneijen/project/data/em-maps/$complex'.info'`

    sed -i "s/em_resolution=10.0/em_resolution=$resolution/g" run.cns
    sed -i 's/em_rest=false/em_rest=true/g' run.cns
# increase runtime as EM runs take longer 
    if [[ $complex == 3J95 ]] || [[ $complex == 5GRS ]] || [[ $complex == 5HNY ]] || [[ $complex == 6AHF ]] || [[ $complex == 6N1Q ]] || [[ $complex == 6IRF ]] || [[ $complex == 6N8Z ]]; then
        sed -i 's/short/medium/g' run.cns
    else
        sed -i 's/short/long/g' run.cns
    fi

else

    if [[ $complex == 6C3P ]] || [[ $complex == 5N5Z ]] || [[ $complex == 3J96 ]]; then
        sed -i 's/short/medium/g' run.cns
    fi
fi


# alter run parameters
 # number of structures
sed -i 's/structures_0=1000/structures_0=50/g' run.cns
sed -i 's/structures_1=200/structures_1=50/g' run.cns
sed -i 's/anastruc_1=200/=anastruc_1=50/g' run.cns

 # account for DNA chain in structure 5Y3R
if [[ `pwd` == *"5Y3R"* ]]; then
    sed -i 's/dna_mol4=false/dna_mol4=true/g' run.cns 
fi 

 # expand protocol
sed -i 's/expand=false/expand=true/g' run.cns
sed -i 's/randangle=6/randangle=0/g' run.cns
sed -i 's/expansion=0.2/expansion=0.05/g' run.cns

 # disable random start
sed -i 's/randorien=true/randorien=false/g' run.cns 
sed -i 's/crossdock=true/crossdock=false/g' run.cns

 # no it0
sed -i 's/ntrials=5/ntrials=1/g' run.cns
sed -i 's/rigidmini=true/rigidmini=false/g' run.cns

# add ligand topologies
for dir in ../ligands/*_prodrg; do
    id=$(echo $dir | cut -d "_" -f 1 | cut -d "/" -f 3)
    cat $(echo $dir/$id).PAR >> toppar/ligand.param
    cat $(echo $dir/$id).TOP >> toppar/ligand.top
done

# start haddock
haddock2.4 >&haddock.out &

