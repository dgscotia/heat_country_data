"""
input = raw data sets downloaded from NRCan
output = Canada sheet and series for plotting
"""

import pandas as pd
import matplotlib.pyplot as plt
gas = 'Natural Gas'
oil = 'Heating Oil'
other = 'Other1'
elec = 'Electricity'

fuel_res_path = "raw_data/Canada/res_ca_e_1.xls"
app_res_path = "raw_data/Canada/res_ca_e_2.xls"
fuel_com_path = "raw_data/Canada/com_ca_e_1.xls"
app_com_path = "raw_data/Canada/com_ca_e_4.xls"


def process_data(filepath):
    data = pd.read_excel(filepath).dropna(
        how="all").drop([3, 5, 6], axis='index').fillna(0)
    data.set_index('Unnamed: 1', inplace=True)
    data.columns = data.iloc[0].astype(int)
    data = data.drop(data.columns[0], axis=1)[1:]
    return data


fuel_res = process_data(fuel_res_path)
app_res = process_data(app_res_path)
fuel_com = process_data(fuel_com_path)
app_com = process_data(app_com_path)


def sum_elec_for_heat(year):
    "Sums the electricity used for appliances, lighting and space cooling"
    res = fuel_res[2:8][year][elec] - sum(app_res[2018][4:7].values)
    com = fuel_com[2:8][year][elec] - sum(app_com[2018][4:9].values)
    return res + com


# These data are from the International Energy Agency's public statistics on electricity production in Canada.
renewable_share = 433242/653669


def create_summary_dict(year):
    summary_dict = {
        'Fossil gas': fuel_res[3:8][year]["Natural Gas"] + fuel_com[3:8][year]["Natural Gas"],
        'Oil products': fuel_res[3:8][year]["Heating Oil"] + fuel_com[3:8][year]["Light Fuel Oil and Kerosene"] + fuel_com[3:8][year]["Heavy Fuel Oil"],
        'Other fossil fuels': fuel_res[3:8][year][other] + fuel_com[3:8][year]["Steam"] + fuel_com[3:8][year][other],
        'Direct renewables': fuel_res[3:8][year]["Wood"],
        'Heat pumps': 0,  # add heat pumps in later
        'District heat': 0,
        'Electricity': sum_elec_for_heat(year),
        'Non-renewable electricity': sum_elec_for_heat(year)*(1-renewable_share),
        'Renewable electricity': sum_elec_for_heat(year)*renewable_share,
        'Renewable district heat': 0,
        'Ambient heat': 0
    }
    return summary_dict


years = fuel_res.columns
total = {year: create_summary_dict(year) for year in years}

total_df = pd.DataFrame(total).T

plot_1_filt = ['Fossil gas', 'Oil products', 'Other fossil fuels',
               'Direct renewables', 'Heat pumps', 'District heat', 'Electricity']
plot_2_filt = ['Fossil gas', 'Oil products', 'Other fossil fuels', 'Direct renewables',
               'Non-renewable electricity', 'Renewable electricity', 'Renewable district heat', 'Ambient heat']

plot_1_data = total_df[plot_1_filt]
plot_2_data = total_df[plot_2_filt]
