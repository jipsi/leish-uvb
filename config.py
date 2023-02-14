import scanpy as sc
import anndata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import cell2location
import scvi

from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42

results_folder = '.'
#relative path to where visium data lives
sp_data_folder = '.'

# create paths and names to results folders for reference regression and cell2location models
ref_run_name = './reference_signatures'
run_name = f'{results_folder}/cell2location_map'

libraries = ["62_E2"]

sample_list = 'sd22.5.3.csv'

exec(open("train_ref.py").read())