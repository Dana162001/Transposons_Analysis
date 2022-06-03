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
## About The Project

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

### Docker 
1. Create `YOUR_DATA_ROOT` directory on your local machine
   ```
   mkdir /YOUR_DATA_ROOT
   ```
2. Docker run! `-u $(id -u):$(id -g)` is used to make sure all files created by pipeline are accessible for users
   ```
   docker run -it -u $(id -u):$(id -g) -v /YOUR_DATA_ROOT:/data dana162001/p_SA /bin/bash
   ```
