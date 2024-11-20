#!/bin/bash

# Request jupyter lab session on RVS
module load $1
cd $HOME/rvs

# Capture the Slurm job ID
job_id=$(sbatch --time=$2 $RVS_HOME/bin/$3.cmd | awk '{print $4}')
echo "Submitted batch job $job_id"

# Append the Slurm job ID to the file $HOME/.jupyter/modules.conf
echo "$job_id" >> $HOME/.jupyter/modules.conf

unset job_id

# Read the job ID from the last line of $HOME/.jupyter/modules.conf
job_id=$(tail -n 1 $HOME/.jupyter/modules.conf)

# Form the path ~/rvs/notification.<slurm job id>
notification_path=~/rvs/notification.$job_id

# Watch for the creation of the notification file
echo "Waiting in queue ..."
while [ ! -f "$notification_path" ]; do
    sleep 1
done

# Parse notification log file and print session URL
session_url=$(grep -Eo 'http[s]?://[^ ]+' "$notification_path" | head -n 1)
echo -e "Batch job $job_id granted. Connect to your session directly using a web browser via\n$session_url"