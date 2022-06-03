# Step by step workflow for composite transposons analysis based on ISEScan


<img src="/figs/workflow_p_sa.jpg">

## Citing
```
@article {Gligorijevic2019,
	author = {Zhiqun Xie, Haixu Tang},
	title = {SEScan: automated identification of Insertion Sequence Elements in prokaryotic genomes},
	year = {2017},
	doi = {10.1093/bioinformatics/btx433},
	URL = {https://academic.oup.com/bioinformatics/article/33/21/3340/3930124},
	journal = {Bioinformatics, Volume 33}
}

```
# About The Project

This pipeline is built to search for **genes that are transferred by transposition** within the bacterial genome. The first step of the algorithm is to search for insertion sequences (that are flunking sequences of transposons) using the **ISEScan** tool. 

Then transposon is made from found ISs by adding coordinates to the original GenBank file. The next task is to extract coding sequences that lie within the transposons in the fasta format. The visualization with Artemis is optional. 

In the next step, all extracted sequences are clustered by CD-HIT, and clusters are filtered depending on the threshold. Finally, one representative sequence is chosen from each cluster and blasted against the database of interest. 

* [ISEScan](https://github.com/xiezhq/ISEScan)
* [CD-HIT](https://anaconda.org/bioconda/cd-hit)
* [Conda](https://docs.conda.io/en/latest/miniconda.html)

# Installation
## Local
1. Setup conda environment

You can install ISEScan to other place by changing the default miniconda3 install path in step **Install Miniconda3**. Visit [Bioconda recipe for ISEScan](https://bioconda.github.io/recipes/isescan/README.html) for more details. 

	
2. Install ISEScan
Automated install by Bioconda (recommended!)

```
conda install -c bioconda isescan
```
Visit [ISEScan Installation](https://github.com/xiezhq/ISEScan) for more details. 

3. Install CD-HIT
```
conda install -c bioconda cd-hit
```

4. Install Artrtemis (optional)
```
conda install -c bioconda artemis
```

## Docker 
1. Create `YOUR_DATA_ROOT` directory on your local machine
   ```
   mkdir /YOUR_DATA_ROOT
   ```
2. Docker run! `-u $(id -u):$(id -g)` is used to make sure all files created by pipeline are accessible for users
   ```
   docker run -it -u $(id -u):$(id -g) -v /YOUR_DATA_ROOT:/data dana162001/p_SA /bin/bash
   ```
# Running pipeline
1. Download/prepear genomes of interest in .gbff format
2. Run script to convert .gbff to .fasta format
   ```
   convert_gb_to_fasta.py -i [Name_of_dir_with_gb_files] -o [Name_of_dir_with_fasta_files]
   ```
3. Run ISEScan 
 ```
 isescan.py --seqfile seq_ID.fasta --output results --nthread 2
```
- By default, ISEScan will use one CPU core but you can change it using command option  ```--nthread [num] ```
4. Run artemis_visualisation.py to add coordinates of new ISs to the original .gbff files
 ```
 artemis_visualisation.py -i [dir_to_ISEScan_results_csv] -u [dir_to_original_gbff_files] -m [dir_to_modified_gbff_files]
```
5. Run me_cds.py to extract coding sequences from modified .gbff files
 ```
 artemis_visualisation.py -i [dir_to_modified_gbff_files]  -o merged_cds_prot.fasta
 ```
6. Run cd_hit.py to cluster extracted sequences
 ```
 cd_hit.py -i [dir_to_merged_cds_prot.fasta]  -o [output_path]
 ```
- Default parameter: -c 0.6 -aS 0.8 -n 4 -M 4000
- -c sequence identity threshold, default 0.9 this is the default cd-hit's "global sequence identity" calculated as: number of identical amino acids in alignment divided by the full length of the shorter sequence
- -aS alignment coverage for the shorter sequence, default 0.0 if set to 0.9, the alignment must covers 90% of the sequence
- -n 4 for thresholds 0.6 ~ 0.7
- - -M max available memory (Mbyte), default 400
 
