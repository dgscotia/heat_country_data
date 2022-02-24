"""
1. Import the datasets
2. Put them into a dataframe
3. Make the pie charts with seaborn


"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

df_1 = pd.read_csv("heat_data_fig_1_python.csv").set_index("Country")
df_2 = pd.read_csv("heat_data_fig_2_python.csv").set_index("Country")


""" FIGURE PROPERTIES """

font = 'Microsoft Yi Baiti'
text_props = {'fontsize': 25, 'fontname': font}
title_props = {'fontsize': 35, 'fontname': font,
               'verticalalignment': 'baseline'}
legend_pie_props = {'size': 20, 'family': font}
legend_bar_props = {'size': 25, 'family': font}
matplotlib.rcParams['font.family'] = font
matplotlib.rcParams["figure.facecolor"] = "w"
face_color = "white"
pie_size = (14, 14)
bar_size = (20, 12)
bar_font = 30

""" FIGURE COLOURS """

gas = '#8c564b'
oil = '#7f7f7f'
other_fossils = '#c7c7c7'
heat_pumps = '#c5b0d5'
direct_re = '#2ca02c'
district_heat = '#d62728'
electricity = '#1f77b4'
non_re_elec = '#ffbb78'
re_elec = '#98df8a'
re_DHC = '#d62728'
ambient = '#17becf'

colors_1 = [gas, oil, other_fossils, heat_pumps,
            direct_re, district_heat, electricity]
colors_2 = [gas, oil, other_fossils, non_re_elec,
            re_elec, direct_re, re_DHC, ambient]


labels_1 = df_1.columns
labels_2 = df_2.columns
plot_1 = [df_1, colors_1, labels_1, F"What fuels are used in ", "fig_1"]
plot_2 = [df_2, colors_2, labels_2, "How clean is the heat in ", "fig_2"]


def plot_country(country, df, colors, labels, title, name):
    fig = plt.figure(figsize=pie_size)
    plt.pie(df.loc[country], colors=colors, startangle=90, autopct=lambda p: '{:.0f}%'.format(
        round(p)) if p > 0 else '', textprops=text_props)
    plt.title(title+f"{country}?", fontdict=title_props, y=0.95)
    plt.legend(labels=labels, prop=legend_pie_props, loc=8,
               ncol=3, edgecolor='white', framealpha=0)
    centre_circle = plt.Circle((0, 0), 0.70, fc=face_color)
    ax = fig.gca()
    ax.add_artist(centre_circle)
    plt.tight_layout()
    plt.savefig(f"Exported/{country}_{name}")
    plt.show()


def plot_countries():
    for country in df_1.index:
        plot_country(country, *plot_1)

    for country in df_2.index:
        plot_country(country, *plot_2)


def plot_bars(df, colors, labels, title, name):
    df.plot(kind='bar', stacked=True, figsize=(
        bar_size), color=colors, width=0.3)
    plt.legend(handles=reversed(plt.legend().legendHandles), labels=reversed(
        labels), bbox_to_anchor=(1.15, 0.5), prop=legend_bar_props, loc=9, ncol=1, framealpha=0)
    plt.grid(alpha=0.4, axis='y')
    plt.title(title, fontdict=title_props, y=1.05)
    plt.xlabel(xlabel='', fontdict=text_props)
    plt.xticks(rotation=45, fontfamily=font, fontsize=bar_font)
    plt.ylabel('Share', fontfamily=font, fontsize=bar_font)
    plt.yticks(fontfamily=font, fontsize=bar_font)
    plt.margins(y=0)
    plt.tight_layout()
    plt.savefig(f"Exported/all_countries_{name}")
    plt.show()


def normalize(df):
    tot = df.sum(axis=1)
    for col in df:
        df[col] /= tot
    return df


df_1_share = normalize(df_1)
df_2_share = normalize(df_2)

order_1 = ["Scotland", "United Kingdom", "Canada",
           "United States", "Germany", "France", "Denmark"]  # most gas
order_2 = ["Denmark", "France", "Germany", "Canada", "Scotland",
           "United States", "United Kingdom"]  # highest RE share

df_1_share = df_1_share.reindex(order_1)
labels_1 = df_1_share.columns

df_2_share = df_2_share.reindex(order_2)
labels_2 = df_2_share.columns

plot_share_1 = [df_1_share, colors_1, labels_1,
                "What fuels are used to heat?", "fig_1"]
plot_share_2 = [df_2_share, colors_2, labels_2,
                "How clean is the heat?", "fig_2"]


if __name__ == "__main__":
    plot_countries()
    plot_bars(*plot_share_1)
    plot_bars(*plot_share_2)
