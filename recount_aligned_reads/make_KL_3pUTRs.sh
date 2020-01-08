#!/bin/bash

#need to add samtools to path unless you already have it in your bashrc
#export PATH="home/lab/samtools/bin:$PATH"

genome_dir=~/genomes/klac_20170819/KL_GTF/
kl_genome=${genome_dir}Kluyveromyces_lactis.ASM251v1.32.gtf

bam_dir=~/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/KL_bams/

#makes peak table using macs2
macs2-stranded -n kl_utrs ${bam_dir}*.bam

#extends 3'UTR using peak table and extension length of 400bp (based on S.Cer 3'UTR length)
gtf-extend --ext-3p 400 -g $kl_genome -p ./kl_utrs_peaks.narrowPeak -o ${genome_dir}Kluyveromyces_lactis.ASM251v1.32.UTR.gtf --extns-out kl_UTRs.extens 
