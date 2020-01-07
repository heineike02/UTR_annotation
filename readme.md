# UTR_annotation

This code provides the scripts used to add UTR annotation to the S.cerevisiae reference genome from [1] and also to artificially extend gene 
annotations for the K. lactis reference genome in order to analys RNA seq expression data from [2].

## Getting Started

### S. cerevisiae annotation 

run Scer_utr_annotation.ipynb in jupyter.  It requires that the script merge_Nag_scerR64.sh is run as an intermediate step on a unix machine. 

Required data files: 
	saccharomyces_cerevisiae_R64-2-1_20150113.gff : original annotation file downloaded from SGD
	Nagalakshmi_2002_3UTRs_V64.gff3 : 3' UTR annotation file downloaded from SGD

Final output file: 
	saccharomyces_cerevisiae_R64-2-1_20150113_UTRs.gff


### K. lactis annotation artificial extension: 


Required data files are: 
	


## References

[1] Heineike BM, El-Samad HJ. Paralogs in the PKA regulon traveled different evolutionary routes to divergent expression in budding yeast. BioRxiv [Preprint]. 2019 bioRxiv 860981 [posted 2019 Dec 02]. Available from: https://www.biorxiv.org/content/10.1101/860981v1 doi: 10.1101/860981.
[2] Nagalakshmi, U., Wang, Z., Waern, K., Shou, C., Raha, D., Gerstein, M., Snyder, M., 2008. The Transcriptional Landscape of the Yeast Genome Defined by RNA Sequencing. Science 320, 1344–1349. https://doi.org/10.1126/science.1158441

## Authors

* **Benjamin Heineike** [heineike02](https://github.com/heineike02)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
