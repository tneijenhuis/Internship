#/bin/bash

#name of the full run directory after creation with run.param as positional arg 
protocol=$1
complex_list=$(ls . | grep -v [a-z])
running=()
finnished=()
simulrun=2

#initialize the total runs
totalruns=0
for i in ${complex_list[@]}; do
 totalruns=$((totalruns+1)) 
done

waittime=900
home=$(pwd)

until [[ ${#finnished[@]} -ge $totalruns ]]; do
    echo Complexes to be docked: ${complex_list[@]} >> $protocol.debug
    temp_complex_list=()
    for complex in ${complex_list[@]}; do 
#starting new runs if maximal paralel jobs has not been reached 
    if [[ ${#running[@]} -lt $simulrun ]]; then
        cd $home/$complex/$protocol
        if [ -f haddock.out ]; then
            echo already started #check if run already started
        else
            bash /home/tneijen/project/scripts/run_haddock.sh
    fi
    cd $home
    echo $complex started at `date` >> $protocol.info
    running=("${running[@]}" "$complex")
  
  else
   temp_complex_list=("${temp_complex_list[@]}" $complex)
  fi
 done 
 complex_list=() 
 complex_list=${temp_complex_list[@]}
 echo Running docking runs: ${running[@]} >> $protocol.debug

 sleep $waittime

# checking for finnished runs
 temp_running=()
 for complexrun in ${running[@]}; do
  if grep -Fxq "Bye bye." $complexrun/$protocol/haddock.out; then
   finnished=("${finnished[@]}" $complexrun)
   echo $complexrun finnished at `date` >> $protocol.info 
   if [ -f $complexrun/$protocol/structures/it1/water/analysis/DONE ]; then
    echo -- and was succesfull >> $protocol.info
   else
    echo -- but failed >> $protocol.info
   fi
# clean run directory as this does not always happen   
   cd $complexrun/$protocol
   tools/haddock-clean
   cd ../..
  else
   temp_running=("${temp_running[@]}" $complexrun)
  fi
 done  
# Reinit running
 running=()
 for temp in ${temp_running[@]}; do
  running=("${running[@]}" $temp)
 done
 echo Finished docking runs: ${finnished[@]} >> $protocol.debug 
done
echo All runs finnished: $totalruns >> $protocol.debug
