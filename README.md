# Project: leish-uvb (instructions)
## Code to replicate the figures in the manuscript (please note the following instructions)

### OS
Windows: Windows 10 x64
Mac
Linux

### Software requirements

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


#### 1. Please maintain folder structure as per the repository

#### Option1 : Start from scratch using raw 10x files (available post publication)
- Download all samples/10x files from GSMXXXX into source/'sample_name'/
- Start with integrated_prepare_rds.Rmd

#### Option2 : Start from prepared Rds containing primary clustering analysis
- Download Rds from googledrive link into your working directory
- Start with integrated_downstream.Rmd

#### For figures relating to ligand-receptor interactions using cellchat, please start with cellchat.Rmd

## UVB light exposure drives effector T cell responses and modifies skin stromal-immune crosstalk during L. donovani infection (unpublished)

Marcela Montes de Oca1#, Shoumit Dey1#, Katrien Van Bocxlaer1, Helen Ashwin1, Najmeeyah Brown1, Elmarie Myburgh1, Nidhi S Dey1, Gulab F Rani1, Edward Muscutt1, Mohamed Osman1, Damian Perez-Mazliah1, Sally James2, Lesley Gilbert2, Mitali Chatterjee3 and Paul M Kaye1

1 York Biomedical Research Institute, University of York, Heslington, YO10 5DD, York, UK
2 Genomics Laboratory, Bioscience Technology Facility, University of York, Heslington, YO10 5DD, York, UK
3 Dept. of Pharmacology, Institute of Postgraduate Medical Education & Research, Kolkata, 700 020, India
'#' These authors contributed equally.

#### Currently available as a pre-print on bioRxiv:  https://www.biorxiv.org/content/10.1101/2023.02.03.526940v1

### Background: 
The steady state balance between stromal and immune cells can be perturbed by environmental stimuli such as UVB light. Little is known about how UVB changes stromal-immune cell cross talk during skin infection.  

### Methods: 
We used a novel murine model of Leishmania donovani infection whereby mice are pre-conditioned and maintained with minimally-erythematous UVB exposure. We used flow cytometry, single-cell RNA sequencing and spatial transcriptomics to examine skin cell phenotype before and after UVB exposure, infection or a combination of both. We further used ligand-receptor databases and computational tools to interpret pathways of cellular cross-talk. 

### Results: 
We report a cell atlas of C57BL/6 mouse skin following UVB exposure, L. donovani infection and the combination of both. We characterise single cells (FACS and scRNA-seq) and predict spatial location using the 10X Genomics Visium platform. We identify phenotypic differences between groups to show that under conventional conditions (non-UVB exposed) Ccl2 transcripts are globally upregulated and CD45-Ter119-CD31-PDPN+ stromal cells increase in abundance in skin of mice infected with L. donovani. UVB exposure alone induces changes to gene signatures associated with metabolic change, notably upregulation of oxidative phosphorylation in macrophages, T cells and fibroblasts. UVB exposure alters immune cell profile of infected mice, with an increase in the abundance of Ifng+ T cells and a shift in predicted pathways of intercellular communication.  In infected, non-UVB exposed mice, the Cd34–Selp pathway was predicted to be the dominant route of communication between fibroblasts, T cells and endothelial cells. However, in UVB-exposed infected mice, this was replaced by Itgb2-Icam2 signalling, with heightened expression of Itgb2 on Ifng+ T cells. 

### Conclusion: 
We show that UVB exposure can significantly modify the cellular landscape and mode of intercellular communication in the skin during L. donovani infection. Our data exemplify the potential importance of including UVB pre-exposure in translational models of cutaneous infection.
