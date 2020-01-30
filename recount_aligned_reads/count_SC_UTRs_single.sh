#!/bin/bash

#Activate python environment for htseq-count
. activate /home/lab/envs/seqanalysis

resource_dir=~/genomes/scer_20181114/
annotation=saccharomyces_cerevisiae_R64-2-1_20150113_UTRs_pelechano_max.gff

bam_dir=~/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/SC_01/star_out/B01_S1_L001_R1_001.fastq.gz/

bam=${bam_dir}starAligned.sortedByCoord.out.bam

htseq-count -t CDS_3pUTR -i Parent -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_counts_UTR_pel_long.txt

