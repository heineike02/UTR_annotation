#This file recounts alignmend data processed in bluebee using htseq_count and the new UTR file (saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff) created in UTR_annotation/Scer_utr_annotation.ipynb
import os
import sys

UTR_param = sys.argv[1] #label for reprocessed files

#'nag' uses 3'UTR annotation from nagalakshmi et al 2008
#'orig' uses original SGD annotation (with chromosome names changed)
# 
#See UTR_annotation/Scer_utr_annotation for details

resource_dir = "/home/heineike/genomes/scer_20181114/"

#(annotation, 
# readcount_ext: extension for count files, 
# featuretype: featuretype to use for counts,
# count_id: attribute to use for ids in countfile
#)
annotation_params = {'nag': ("saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff", 'UTR_nag', 'gene', 'ID'),
               'orig': ("saccharomyces_cerevisiae_R64-2-1_20150113_unique_ids.gff",'orig','gene','ID'),
               'pel': ("saccharomyces_cerevisiae_R64-2-1_20150113_UTRs_pelechano_max.gff", 'UTR_pel','CDS_3pUTR','Parent')
               }

(annotation, readcount_ext, featuretype, count_id)  = annotation_params[UTR_param]
               
processed_data_dir = os.path.normpath("/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/")
samples = os.listdir(processed_data_dir)

for sample in samples: 
    sample_spec = sample.split('_')[0]
    sample_no = sample.split('_')[1]
    if (sample_spec=='SC'): 
        bam_dir = processed_data_dir + os.sep + sample + os.path.normpath("/star_out/B" + sample_no + "_S" + str(int(sample_no)) +"_L001_R1_001.fastq.gz") + os.sep
        bam = bam_dir + 'starAligned.sortedByCoord.out.bam'
        htseq_count_cmd = ['htseq-count',
                                  '-t ' + featuretype, 
                                  '-i ' + count_id, 
                                  '-m intersection-nonempty', 
                                  '-s yes',
                                  '-f bam',
                                  '-r pos',
                                  bam,
                                  resource_dir + annotation, 
                                  '>', 
                                  bam_dir + 'read_counts_' + readcount_ext + '.txt'
                           ]
        
        print(' '.join(htseq_count_cmd))
        os.system(' '.join(htseq_count_cmd))

#htseq-count -t gene -i ID -m intersection-nonempty -s yes -f bam -r pos $bam $resource_dir$annotation > $bam_dir/read_coun    ts_UTR.txt