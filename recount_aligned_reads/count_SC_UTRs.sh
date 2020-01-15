#!/bin/bash

echo 'This can take a long time - you may want to run it from screen' 

#Activate python environment for htseq-count
. activate /home/lab/envs/seqanalysis

#Run the python file which counts .bam files from bluebee using the .gff which contains the 3'UTR from Nagalakshmi 2008 

#prior to running this, go into /recount_sc.py and edit the directory where your BAM files are located and where you want to store them. 

#recounts reads using SGD annotation (should be very close to the bluebee output)
python ./recount_sc.py orig

#recounts reads using updated UTRs on SGD annotation
python ./recount_sc.py nag



#The key command in that file is: 
#htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_counts_UTR.txt

