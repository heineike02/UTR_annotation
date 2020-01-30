#!/bin/bash

echo 'This can take a long time - you may want to run it from screen' 

#Activate python environment for htseq-count
. activate /home/lab/envs/seqanalysis

#Runs recount_sc.py which counts reads from .bam files generated using the bluebee pipeline.
#The file has the option to use different .gff feature files. 
#
#edit recount_sc.py to point to the directory where your BAM files are located and 
#where you want the output to go. 
#
#pel: uses 3'UTRs generated from max extent of the longest transcript identified in 
#Pelechano et al 2013 as curated by SGD.  See UTR_annotation/Scer_annotation_tif.ipynb.
#saccharomyces_cerevisiae_R64-2-1_20150113_UTRs_pelechano_max.gff
#
#nag: Uses gene annotations which are extended to the length of the 3'UTR database based 
#on Nagalakshmi 2008 as curated on SGD.  See UTR_annotation/Scer_annotation_nag.ipynb
#saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff
#
#orig: Uses gff that has chromosomes renamed, and cleaned in UTR_annotation/Scer_annotation_tif.ipynb.
#saccharomyces_cerevisiae_R64-2-1_20150113_unique_ids.gff

#recounts reads using SGD annotation (should be very close to the bluebee output)
python ./recount_sc.py orig

#recounts reads using updated UTRs on SGD annotation
python ./recount_sc.py pel # nag



#The key command in that file is: 
#htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_counts_UTR.txt

