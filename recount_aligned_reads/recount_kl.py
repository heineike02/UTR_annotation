import os
import sys

N_ext = 400

resource_dir = "/home/heineike/genomes/klac_20170819/KL_GTF/"
annotation = "Kluyveromyces_lactis.ASM251v1.32_UTR_" + str(N_ext) + ".gtf"
processed_data_dir = os.path.normpath("/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/")
samples = os.listdir(processed_data_dir)

for sample in samples: 
    sample_spec = sample.split('_')[0]
    sample_no = sample.split('_')[1]
    if (sample_spec=='KL'):   # and (sample_no != '01'):
        print('processing ' + sample_spec + '_' +  sample_no)
        bam_dir = processed_data_dir + os.sep + sample + os.path.normpath("/star_out/B" + sample_no + "_S" + str(int(sample_no)) +"_L001_R1_001.fastq.gz") + os.sep
        bam = bam_dir + 'starAligned.sortedByCoord.out.bam'
        htseq_count_cmd = 'htseq-count -m intersection-nonempty -s yes -f bam -r pos ' + bam + ' ' + \
                          resource_dir + annotation+ ' > ' + bam_dir + 'read_counts_UTR_' + str(N_ext) + '.txt'
        os.system(htseq_count_cmd)

