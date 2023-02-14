# Project: leish-uvb (instructions)
## Software requirements: 

### OS
Windows: Windows 10 x64 (For all R based code)
Mac
Linux: CentOS Linux 7 Core (For all Python scripts running cell2location)

### Software 

#### 1. R version 4.2.2
#### 2. Packages required - see session information below

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

#### 3. Additional packages required for spatial analysis, cellchat and preparing data for cell2location
#### 4. Packages required - see session information below

## Code to replicate the figures in the manuscript (please note the following instructions)

#### 1. Please maintain folder structure as per the repository

#### Option1 : Start from scratch using raw 10x files (available post publication)
- Download all samples/10x files from GSMXXXX into source/'sample_name'/
- Start with integrated_prepare_rds.Rmd

#### Option2 : Start from prepared Rds containing primary clustering analysis
- Download Rds from googledrive link into your working directory
- Start with integrated_downstream.Rmd

#### For figures relating to ligand-receptor interactions using cellchat, please start with cellchat.Rmd

## UVB modifies skin immune-stroma cross-talk and promotes effector T cell recruitment during cryptic Leishmania donovani infection 

Marcela Montes de Oca^1#^, Shoumit Dey^1#^, Katrien Van Bocxlaer^1^, Helen Ashwin^1^, Najmeeyah Brown^1^, Elmarie Myburgh^1^, Nidhi S Dey^1^, Gulab F Rani^1^, Edward Muscutt^1^, Mohamed Osman^1^, Damian Perez-Mazliah^1^, Sally James^2^, Lesley Gilbert^2^, Mitali Chatterjee^3^ and Paul M Kaye^1^

1 York Biomedical Research Institute, University of York, Heslington, YO10 5DD, York, UK
2 Genomics Laboratory, Bioscience Technology Facility, University of York, Heslington, YO10 5DD, York, UK
3 Dept. of Pharmacology, Institute of Postgraduate Medical Education & Research, Kolkata, 700 020, India
'#' These authors contributed equally.

#### Currently available as a pre-print on bioRxiv:  https://www.biorxiv.org/content/10.1101/2023.02.03.526940v1

### Summary: 
Many parasites of significant public health importance assume skin residency without causing overt pathology. How immune and stromal cells respond to such “cryptic” infections and how exposure to UVB alters such responses in poorly understood. We combined scRNA-seq, spatial transcriptomics and inferential network analysis to address these questions in a model of cryptic skin infection by Leishmania donovani. In infected C57BL/6 mice, p-selectin and CXCL12 interactions dominate intercellular communication between leucocytes, fibroblast and endothelial cells, but effector T cell function remains muted. Following UVB exposure, increased numbers of IFNγ+ CD4+ Th1 cells and NK cells enter the skin, communicating with stromal cells via CCL5-CCR5 and LFA-1-ICAM1/2. However, spatial mapping indicated that Th1 cells and macrophages occupied distinct niches after UVB exposure, likely limiting effector function. Our data provide the first holistic view of the immune landscape during cryptic L. donovani infection and demonstrate how UVB exposure fundamentally reshapes this response.
