"""
input = raw data sets downloaded from NRCan
output = Canada sheet and series for plotting
"""


import pandas as pd

fuel_res = pd.read_excel("raw_data/Canada/res_ca_e_1.xls")
print(fuel_res)
