#!/bin/bash 

#To run file type ./merge_Nag_scerR64.sh saccharomyces_cerevisiae_R64-2-1_20150113 

#convert to BED file
base_name=$1

#"scer_ref_test"

fname_in=$1_nagdata_UTRchildren

#Sort out combined file including UTR and annotation
bedtools sort -i $fname_in.gff > ${fname_in}_sorted.gff 

#Merge coordinates to get new coordinates for gene
bedtools merge -s -d 10 -i ${fname_in}_sorted.gff -c 1,9 -o count,collapse -delim ";" >  ${fname_in}_merged

cp ${fname_in}_sorted.gff ~/bioinformatics/Bioinformatics/genome_assembly/
cp ${fname_in}_merged ~/bioinformatics/Bioinformatics/genome_assembly/

#In the future I should add one to the start for the merged items because the 
#bedtools merge subtracted one. 
#awk '{OFS="\t"
#if ($4 = "+")
#{ print $1,$2+1,$3,$4,$5,$6}
#else 
#{ print $0}
#}' ${fname_in}_merged > ${fname_in}_merged2

