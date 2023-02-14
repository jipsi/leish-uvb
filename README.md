# Project: leish-uvb (instructions)
## Software requirements: 

### OS
- Windows: Windows 10 x64 (For all R based code)
- Mac
- Linux: CentOS Linux 7 Core (For all Python scripts running cell2location)

### Software 


#### 1. R version 4.2.2
#### 2. RStudio 2022.02.3+492 (Optional)
#### 3. Package versioning required - see session information below

> sessionInfo()
> R version 4.2.2 (2022-10-31 ucrt)
> Platform: x86_64-w64-mingw32/x64 (64-bit)
> Running under: Windows 10 x64 (build 19045)
> 
> Matrix products: default
> 
> locale:
> [1] LC_COLLATE=English_United Kingdom.utf8  LC_CTYPE=English_United Kingdom.utf8    LC_MONETARY=English_United Kingdom.utf8
> [4] LC_NUMERIC=C                            LC_TIME=English_United Kingdom.utf8    
> 
> attached base packages:
> [1] stats     graphics  grDevices utils     datasets  methods   base     
> 
> other attached packages:
>  [1] reshape2_1.4.4     ggpubr_0.5.0       sqldf_0.4-11       RSQLite_2.2.20     gsubfn_0.7         proto_1.0.0        stringr_1.5.0     
>  [8] ggplot2_3.4.0      dplyr_1.0.10       cowplot_1.1.1      SeuratObject_4.1.3 Seurat_4.3.0 

#### 3. Additional packages required for spatial analysis, cellchat (https://github.com/sqjin/CellChat) and preparing data for cell2location (https://cell2location.readthedocs.io/en/latest/)
Reported as sessionInfo()
> other attached packages:
> [1] wordcloud_2.6       RColorBrewer_1.1-3  ggalluvial_0.12.3   NMF_0.25            cluster_2.1.4       rngtools_1.5.2      registry_0.5-1        stringr_1.5.0      
> [9] SeuratObject_4.1.3  Seurat_4.3.0        patchwork_1.1.2     CellChat_1.6.1      Biobase_2.58.0      BiocGenerics_0.44.0 ggplot2_3.4.0        igraph_1.3.5       
> [17] dplyr_1.0.10  
#### 4. RUNNING TIME: All R files run sequentially will take approximately 1.5 hours to run on a windows computer with 64GB RAM on a 8 core 3.00GHz machine (eg. processor Intel(R) Core(TM) i7-9700 CPU)

## Code to replicate the figures in the manuscript (please note the following instructions)

#### 1. Code will attempt to create folder structure as showing in the repository. Please maintain folder structure as per the repository for the plots/Rds files to save in the correct folders. Download all Rds files from https://zenodo.org/record/7638456 to your working folder as mentioned in each step.

#### 2. To see how the data is integrated please look at integrated_prepare_rds.Rmd. However the raw data will be made available upon publication but please use the Rds file link below to load the integrated data for inspection, analysis or re-creating figures in <u>'Option 2'</u> below

##### Option1 : Start from scratch using raw 10x files (available post publication)
- Download all samples/10x files from GSMXXXX into source/'sample_name'/
- Start with integrated_prepare_rds.Rmd

##### Option2 : Start from prepared Rds containing primary clustering analysis
- Download Rds integrated_mm2108_dims15_res0.4.rds (Single cell RNA seq) from https://zenodo.org/record/7638456 into your working directory
- Start with integrated_downstream.Rmd
- This file will take approximately 25-30 minutes to run from start to finish on a windows computer with 64GB RAM on a 8 core 3.00GHz machine (eg. processor Intel(R) Core(TM) i7-9700 CPU)

#### 3. For spatial data: To see how the data is integrated please look at integrated_spatial_prepare_rds.Rmd. However the raw data will be made available upon publication but please use <u>'Option 2'</u> using the Rds file (link below) to load the integrated data for inspection, analysis or re-creating figures in  below.

##### Option1 : Start from scratch using raw 10x files (available post publication)
- Download all samples/10x files from GSMXXXX into source/'Visium_slide_name'/
- Start with integrated_spatial_prepare_rds.Rmd

##### Option2 : Start from prepared Rds containing primary clustering analysis
- Download Rds only_mm2108_skin_merged.rds (Single cell RNA seq) from https://zenodo.org/record/7638456 into your working directory
- Download q05_cell_abundance_w_sf_barcoded.csv from repository to your working directory
- Start with integrated_spatial_cell2location.Rmd
- This file will take approximately 5-10 minutes to run from start to finish on a windows computer with 64GB RAM on a 8 core 3.00GHz machine (eg. processor Intel(R) Core(TM) i7-9700 CPU)

#### 4. For figures relating to ligand-receptor interactions using cellchat, please start with cellchat.Rmd. 
- Please follow the instructions in the code, most importantly after setting up folders and loading libraries please make sure the following Rds files are stored in the respective folders
- cellchat_Untd_d0.rds
- cellchat_Untd_INF.rds
- cellchat_UVB_d0.rds
- cellchat_UVB_INF.rds
- Files are available at the zenodo link: https://zenodo.org/record/7638456
- When re-running cellchat (see chunks below figure outputs in cellchat.Rmd), this file will take approximately 25-30 minutes to run from start to finish on a windows computer with 64GB RAM on a 8 core 3.00GHz machine (eg. processor Intel(R) Core(TM) i7-9700 CPU)

#### 5. Cell2location: Generating q05_cell_abundance_w_sf_barcoded.csv
### Cell2location v0.1 (https://cell2location.readthedocs.io/en/latest/) was run by following the instructions as per the tool's tutorial for [mapping lymph nodes](https://cell2location.readthedocs.io/en/latest/notebooks/cell2location_tutorial.html). The code was run on University of York's HPC, namely, Viking using GPU node with 1 GPU, 1 node utilising 40GB RAM in approximately 2.5 hours. 1 hour for reference modelling and 1.5 hours for modelling the spatial data to calculate cell abundances in Visium spots 
- Cell2location was installed in its own environment as per the instructions
- RAW single cell data (this study) and RAW spatial data (this study) was used as input to cell2location
- Output was stored as a model.pt file and anndata file containing q05 abundances as metadata
- Python scripts were submitted to a job manager on the HPC as a shell script
> -#!/bin/bash
> -#SBATCH --job-name=XXXX
> -#SBATCH --mail-type=END
> -#SBATCH --mail-user=shoumit.dey@york.ac.uk
> -#SBATCH --ntasks=1
> -#SBATCH --cpus-per-task=1
> -#SBATCH --mem=40gb
> -#SBATCH --time=04:00:00
> -#SBATCH --output=sd22.5.1.log
> -#SBATCH --account=XXXX
> -#SBATCH --partition=gpu
> -#SBATCH --gres=gpu:1
> 
> module load system/CUDA/10.0.130
> module load lang/Miniconda3/4.9.2
> 
> source activate cell2loc_env2
> 
> command -v python
> 
> python config.py
> 
> source deactivate
- Python code used is available in the repository. Running this will require RAW data which will be available on publication. For a demo we have provided one Visium sample (...) and our single cell dataset in 'diet' anndata format here: https://zenodo.org/record/7638456

## UVB modifies skin immune-stroma cross-talk and promotes effector T cell recruitment during cryptic Leishmania donovani infection 

Marcela Montes de Oca<sup>1#</sup>, Shoumit Dey<sup>1#</sup>, Katrien Van Bocxlaer<sup>1</sup>, Helen Ashwin<sup>1</sup>, Najmeeyah Brown<sup>1</sup>, Elmarie Myburgh<sup>1</sup>, Nidhi S Dey<sup>1</sup>, Gulab F Rani<sup>1</sup>, Edward Muscutt<sup>1</sup>, Mohamed Osman<sup>1</sup>, Damian Perez-Mazliah<sup>1</sup>, Sally James<sup>2</sup>, Lesley Gilbert<sup>2</sup>, Mitali Chatterjee<sup>3</sup> and Paul M Kaye<sup>1</sup>

1 York Biomedical Research Institute, University of York, Heslington, YO10 5DD, York, UK
2 Genomics Laboratory, Bioscience Technology Facility, University of York, Heslington, YO10 5DD, York, UK
3 Dept. of Pharmacology, Institute of Postgraduate Medical Education & Research, Kolkata, 700 020, India
'#' These authors contributed equally.

#### Currently available as a pre-print on bioRxiv:  https://www.biorxiv.org/content/10.1101/2023.02.03.526940v1

### Summary: 
Many parasites of significant public health importance assume skin residency without causing overt pathology. How immune and stromal cells respond to such “cryptic” infections and how exposure to UVB alters such responses in poorly understood. We combined scRNA-seq, spatial transcriptomics and inferential network analysis to address these questions in a model of cryptic skin infection by Leishmania donovani. In infected C57BL/6 mice, p-selectin and CXCL12 interactions dominate intercellular communication between leucocytes, fibroblast and endothelial cells, but effector T cell function remains muted. Following UVB exposure, increased numbers of IFNγ+ CD4+ Th1 cells and NK cells enter the skin, communicating with stromal cells via CCL5-CCR5 and LFA-1-ICAM1/2. However, spatial mapping indicated that Th1 cells and macrophages occupied distinct niches after UVB exposure, likely limiting effector function. Our data provide the first holistic view of the immune landscape during cryptic L. donovani infection and demonstrate how UVB exposure fundamentally reshapes this response.
