#!/bin/bash

#Activate python environment for htseq-count
. activate /home/lab/envs/seqanalysis

python ./recount_kl.py

#htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_counts_UTR.txt

