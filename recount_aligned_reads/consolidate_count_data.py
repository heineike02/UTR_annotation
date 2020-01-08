import os
import sys

# python consolidate_count_data.py /home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/ SC nag

## data_dir to start with: "/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/"
## spec start with KL
## UTR param start with 400

#Moves all files into a single directory after reprocessing with new UTR annotations.  
#
# usage: consolidate_count_data.py <data_dir> <species_abbrev> <UTR_param>
# 
# data_dir: directory where 
# species_abbrev: 
#    SC = S. cerevisiae
#    KL = K. lactis
# UTR_param: either nag for SC UTRs calculated using Nagalakshmi paper, or a number representing the arbitrary number of bases added on the end of each transcript in the annotation to represent the UTR. This must be included in the filename of the counts files for each sample (e.g. read_counts_UTR_nag.txt
#
#
# The folder where the data will be moved to will be called
# <data_dir>/counts_UTR_SC_<UTR_pram>

data_dir = os.path.normpath(sys.argv[1])
samples = os.listdir(data_dir + os.sep + "processed_data")

spec = sys.argv[2]
UTR_param = sys.argv[3]

UTR_dir = data_dir + os.sep + 'counts_UTR_'+spec+'_'+UTR_param
       
os.system('mkdir ' + UTR_dir)

for sample in samples: 
    sample_spec = sample.split('_')[0]
    sample_no = sample.split('_')[1]
    if (sample_spec==spec):
        UTR_file_ext = os.sep + "processed_data" + os.sep + sample + os.path.normpath("/star_out/B" + sample_no + "_S" + str(int(sample_no)) +"_L001_R1_001.fastq.gz/read_counts_UTR_" + UTR_param + ".txt")
        UTR_file = data_dir + UTR_file_ext

        cp_cmd = 'cp ' + UTR_file + ' ' + UTR_dir + os.sep + 'read_counts_UTR_'+UTR_param + "_" + sample + '.txt'
        
        os.system('echo ' + sample)  
        #os.system("echo '" + cp_cmd + "'")
        os.system(cp_cmd)