#!/bin/bash

#Activate python environment for htseq-count
. activate /home/lab/envs/seqanalysis

N_ext=200
resource_dir=~/genomes/klac_20170819/KL_GTF/
annotation=Kluyveromyces_lactis.ASM251v1.32_UTR_${N_ext}.gtf

bam_dir=~/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/KL_17/star_out/B17_S17_L001_R1_001.fastq.gz/

bam=${bam_dir}starAligned.sortedByCoord.out.bam

htseq-count -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_counts_UTR_${N_ext}.txt

