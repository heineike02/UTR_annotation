# UTR_annotation

This code provides the scripts used to add UTR annotation to the S.cerevisiae reference genome from \[1] and also to artificially extend gene 
annotations for the K. lactis reference genome in order to analys RNA seq expression data from \[2].

It also contains scripts for recounting raw alignments using the new annotation files for the RNA seq data from \[2]. 

## Getting Started

### S. cerevisiae annotation 

Run `UTR_annotation/Scer_utr_annotation.ipynb` in jupyter.  

Required data files: 

* `saccharomyces_cerevisiae_R64-2-1_20150113.gff` : original annotation file downloaded from SGD
* `Nagalakshmi_2002_3UTRs_V64.gff3` : 3' UTR annotation file downloaded from SGD

Final output file: 

`saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff`


### S. cerevisiae recount

recounts processed data from bluebee using the new UTR counts.  Takes a few minutes to run, so should use unix screen to ensure that it doesn't stop if you lose the connection to the server. 

run `count_SC_UTRs.sh` from command line: `./count_SC_UTRs.sh`

This basically just calls the python file `recount_sc.py` after activating the appropriate conda environment. 

Prior to running the shell script, you should ensure the correct filenames are present for the source data / output in `recount_sc.py`

Inputs:  
bam files with a file structure similar to this: 
`/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/processed_data/SC_02/star_out/B02_S2_L001_R1_001.fastq.gz/starAligned.sortedByCoord.out.bam`

Outputs: 
`read_counts_UTR_nag.txt`

To move all the new count data to an appropriate folder, use 

`consolidate_count_data.py`

Usage: 
`python ./consolidate_count_data.py \<data_dir> \<spec> \<UTR_pram>` 

* data_dir: location of processed data from bluebee e.g. `/home/heineike/rna_seq_data/20181024_KL_SC_PKA_Msn24_Rph1Gis1/dual_index/BMH_HES_02/`
spec: `SC` or `KL`
UTR_param: `nag` or number of arbitrary bases added e.g. `400`

Moves all the new count data to a new folder. 

### K. lactis annotation artificial extension: 


Coming Soon
	


## References

\[1] Heineike BM, El-Samad HJ. Paralogs in the PKA regulon traveled different evolutionary routes to divergent expression in budding yeast. BioRxiv \[Preprint]. 2019 bioRxiv 860981 \[posted 2019 Dec 02]. Available from: https://www.biorxiv.org/content/10.1101/860981v1 doi: 10.1101/860981.

\[2] Nagalakshmi, U., Wang, Z., Waern, K., Shou, C., Raha, D., Gerstein, M., Snyder, M., 2008. The Transcriptional Landscape of the Yeast Genome Defined by RNA Sequencing. Science 320, 1344–1349. https://doi.org/10.1126/science.1158441

## Authors

* **Benjamin Heineike** [heineike02](https://github.com/heineike02)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
