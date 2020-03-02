shopt -s expand_aliases
source /home/sbgrid/programs/sbgrid.shrc

/home/sbgrid/programs/x86_64-linux/phenix/1.14-3260/bin.capsules/phenix.clashscore $1 | grep clashscore | awk '{print $3}'
