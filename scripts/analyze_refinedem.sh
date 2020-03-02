#!/bin/bash

# will analyze the pdb structures, output can be converted to CSV by out2csv.py

script_dir=/home/tneijen/project/scripts/

#make header
echo pdb_id
echo correlation_coefficient
echo interface_clashes
echo clashscore
echo .

echo $1
# correlation coefficient 
bash "$script_dir"calculate_CC.sh $1 | tail -1 
# clashes on interface 
python3 "$script_dir"clash.py $1
# full clashscore
bash "$script_dir"fullclashscore.sh $1 | tail -1
echo .
