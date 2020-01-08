#This file recounts alignmend data processed in bluebee using htseq_count and the new UTR file (saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff) created in UTR_annotation/Scer_utr_annotation.ipynb

import os
import sys

resource_dir = "/home/heineike/genomes/scer_20181114/"
annotation = "saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff"

processed_data_dir = os.path.normpath("/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/")
samples = os.listdir(processed_data_dir)

UTR_param = 'nag'  #label for reprocessed files

#Sample SC_01 used to be filtered out here, but now it is not


for sample in samples: 
    sample_spec = sample.split('_')[0]
    sample_no = sample.split('_')[1]
    if (sample_spec=='SC'):  # and (sample_no != '01'):
        bam_dir = processed_data_dir + os.sep + sample + os.path.normpath("/star_out/B" + sample_no + "_S" + str(int(sample_no)) +"_L001_R1_001.fastq.gz") + os.sep
        bam = bam_dir + 'starAligned.sortedByCoord.out.bam'
        htseq_count_cmd = 'htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos ' + bam + ' ' + \
                          resource_dir + annotation+ ' > ' + bam_dir + 'read_counts_UTR_' + UTR_param + '.txt'
        os.system(htseq_count_cmd)

#htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_coun    ts_UTR.txt