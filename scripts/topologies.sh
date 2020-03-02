#!bin/bash
for i in *.pdb; do
    ~enmr/software/PRODRG/run_prodrg.py $i HADDOCK
#A few lines from the .PAR file need to be removed
    file=$(echo $i | cut -d '.' -f 1)
    cd ${file}_prodrg
    grep -A 4 NBONds ${file}.PAR > remove.txt
    grep -v -f remove.txt ${file}.PAR > ${file}.PAR0
    mv -f ${file}.PAR0 ${file}.PAR
    rm -f remove.txt
    cd ..
done
