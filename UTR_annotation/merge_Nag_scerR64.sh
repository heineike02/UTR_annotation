#!/bin/bash 

#Uses bedtools to sort combined UTR and annotation file and then merges the coordinates of the UTR and previous gene to get new coordinates for gene.  
#
#Inputs: 
#
#fname_base (e.g. /home/heineike/genomes/scer_20181114/saccharomyces_cerevisiae_R64-2-1_20150113)
#
#To run file type ./merge_Nag_scerR64.sh <fname_base>
#
#Requires that the file <fname_base>_nagdata_UTRchildren exist
#
#Outputs: 
#
# <fname_base>_sorted.gff : sorts out combined UTR/annotation file
#
# <fname_base>_merged : coordinates of related features merged to get new gene coordinates. 
#

#convert to BED file
base_name=$1

#"scer_ref_test"

fname_in=$1_nagdata_UTRchildren

#Sort out combined file including UTR and annotation
bedtools sort -i $fname_in.gff > ${fname_in}_sorted.gff 

#Merge coordinates to get new coordinates for gene
bedtools merge -s -d 10 -i ${fname_in}_sorted.gff -c 1,9 -o count,collapse -delim ";" >  ${fname_in}_merged

#cp ${fname_in}_sorted.gff ~/bioinformatics/Bioinformatics/genome_assembly/
#cp ${fname_in}_merged ~/bioinformatics/Bioinformatics/genome_assembly/

#In the future I should add one to the start for the merged items because the 
#bedtools merge subtracted one. 
#awk '{OFS="\t"
#if ($4 = "+")
#{ print $1,$2+1,$3,$4,$5,$6}
#else 
#{ print $0}
#}' ${fname_in}_merged > ${fname_in}_merged2

