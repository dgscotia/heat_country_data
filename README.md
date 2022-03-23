# heat_country_data

This program processes raw national-level data and plots building heat consumption data in matplotlib. Both the jupyter notebook 'heat_notebook.ipynb' and the file 'main.py' are functional.

The raw national-level datasets are included in the folder 'raw_data'. Some datasets have been used but are not yet publicly available. These are noted where possible.

The data from Canada can be processed using in 'canada.py' and imported into 'main.py'. Data from the remaining countries should similarly be processed in python files as well. Currently, they are processed in .xlsx files in the folder 'Processed'.

The processed data are then manually copied into two .csv files: 'heat_data_fig_1_python.csv' and 'heat_data_fig_2_python.csv'. In the future, the processing and preparation of the data to produce the figures should all be done inside the python code. In an ideal case, the raw data would be read through an Application Programming Interface (API) from each national database and used to produce corresponding figures.

## References

### Canada

1. Natural Resources Canada - Residential Sector;[ Table 1: Secondary Energy Use and GHG Emissions by Energy Source]()
2. Natural Resources Canada - Residential Sector;[ Table 2: Secondary Energy Use and GHG Emissions by End-Use](https://oee.nrcan.gc.ca/corporate/statistics/neud/dpa/showTable.cfm?type=CP&sector=res&juris=ca&rn=2&page=0)
3. Natural Resources Canada - Commercial/Institutional Sector;[ Table 1: Secondary Energy Use and GHG Emissions by Energy Source](https://oee.nrcan.gc.ca/corporate/statistics/neud/dpa/showTable.cfm?type=CP&sector=com&juris=ca&rn=1&page=0)
4. Natural Resources Canada - Commercial/Institutional Sector; [Table 4: Secondary Energy Use and GHG Emissions by End-Use](https://oee.nrcan.gc.ca/corporate/statistics/neud/dpa/showTable.cfm?type=CP&sector=com&juris=ca&rn=4&page=0)
5. Additional datasets containing estimates of heating energy from heat pumps shared privately by Natural Resources Canada.

Remaining references can be located in the corresponding .xlsx in the folder "Processed".
