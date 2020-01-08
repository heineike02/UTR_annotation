import os
import sys

# copy KL bam files to a single directory - could do all of them with a symlink

samples_to_move_no = ['18','19','20','21','23','24','25','26']
samples_to_move = ['KL_' + no for no in samples_to_move_no]

data_dir = os.path.normpath("/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/")

for sample in samples_to_move:
    sample_spec = sample.split('_')[0]
    sample_no = sample.split('_')[1]  
    
    
    bam_ext = os.sep + "processed_data" + os.sep + sample + os.path.normpath("/star_out/B" + sample_no + "_S" + str(int(sample_no)) +"_L001_R1_001.fastq.gz/starAligned.sortedByCoord.out.bam")
    bam = data_dir + bam_ext
    output_file = data_dir + '/KL_bams/'+sample + '.bam'
    cp_cmd = 'cp ' + bam + ' ' + output_file
    
    #print(cp_cmd)
    os.system(cp_cmd)