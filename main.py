"""
1. Import the datasets
2. Put them into a dataframe
3. Make the pie charts with seaborn


"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_1 = pd.read_csv("heat_data_fig_1_python.csv").set_index("Country")
df_2 = pd.read_csv("heat_data_fig_2_python.csv").set_index("Country")
fontprops = {'fontsize': 25, 'fontname': 'Microsoft Yi Baiti'}
colors = sns.color_palette("tab20")

labels_1 = df_1.columns
labels_2 = df_2.columns
