import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas dataframe
# df = pd.read_csv('L58.txt', sep='\t')
# df2 = pd.read_csv('R500.txt', sep='\t')
df3 = pd.read_csv('A03.txt', sep='\t')
df4 = pd.read_csv('WO_83.txt', sep='\t')

# Filter the dataframe to keep only the row with geneID 'BraR500.01G000100.v2.1'
# geneID = 'BraR500.10G216000.v2.1' #L58
# geneID2 = 'BraR500.07G194500.v2.1' #L58
# geneID3 = 'BraR500.07G054900.v2.1' #R500
# geneID4 = 'BraR500.03G233800.v2.1' #R500
# geneID5 = 'BraR500.02G384300.v2.1' #A03

geneID = 'BraR500.01G000300.v2.1' #A03
geneID2 = 'BraR500.01G000400.v2.1' #A03
geneID3 = 'BraR500.01G000600.v2.1' #A03

geneID4 = 'BraR500.10G287000.v2.1' #WO_83
geneID5 = 'BraR500.10G287800.v2.1' #WO_83
geneID6 = 'BraR500.10G288200.v2.1' #WO_83

gene_names = [geneID, geneID2, geneID3, geneID4, geneID5, geneID6]

df_filtered = df3.loc[df3['GeneID'] == geneID]
df_filtered2 = df3.loc[df3['GeneID'] == geneID2]
df_filtered_R5 = df3.loc[df3['GeneID'] == geneID3]

df_filtered_R52 = df4.loc[df4['GeneID'] == geneID4]
df_filtered_A = df4.loc[df4['GeneID'] == geneID5]
df_filtered_A2 = df4.loc[df4['GeneID'] == geneID6]

# Check for missing values in the DataFrame
if df_filtered.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered.fillna(df_filtered.mean().mean(), inplace=True)

# Check for missing values in the DataFrame
if df_filtered2.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered2.fillna(df_filtered2.mean().mean(), inplace=True)

# Check for missing values in the DataFrame
if df_filtered_R5.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered_R5.fillna(df_filtered_R5.mean().mean(), inplace=True)

# Check for missing values in the DataFrame
if df_filtered_R52.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered_R52.fillna(df_filtered_R52.mean().mean(), inplace=True)

# Check for missing values in the DataFrame
if df_filtered_A.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered_A.fillna(df_filtered_A.mean().mean(), inplace=True)

# Check for missing values in the DataFrame
if df_filtered_A2.isna().sum().sum() > 0:
    # Replace missing values with the average of all values across all columns
    df_filtered_A2.fillna(df_filtered_A2.mean().mean(), inplace=True)

TP_names = ["TP1", "TP2", "TP3", "TP4", "TP5", "TP6", "TP7"]

# Select the relevant columns and calculate the average and standard deviation
# TP_columns = ['L58_WTP1_R1', 'L58_WTP1_R2', 'L58_WTP1_R3', 'L58_WTP1_R4',
#               'L58_WTP2_R1', 'L58_WTP2_R2', 'L58_WTP2_R3', 'L58_WTP2_R4',
#               'L58_WTP3_R1', 'L58_WTP3_R2', 'L58_WTP3_R3', 'L58_WTP3_R4',
#               'L58_WTP4_R1', 'L58_WTP4_R2', 'L58_WTP4_R3', 'L58_WTP4_R4',
#               'L58_WTP5_R1', 'L58_WTP5_R2', 'L58_WTP5_R3', 'L58_WTP5_R4',
#               'L58_WTP6_R1', 'L58_WTP6_R2', 'L58_WTP6_R3', 'L58_WTP6_R4',
#               'L58_WTP7_R1', 'L58_WTP7_R2', 'L58_WTP7_R3', 'L58_WTP7_R4']

# # Select the relevant columns and calculate the average and standard deviation
# TP_columns_R500 = ['R500_WTP1_R1', 'R500_WTP1_R2', 'R500_WTP1_R3', 'R500_WTP1_R4',
#               'R500_WTP2_R1', 'R500_WTP2_R2', 'R500_WTP2_R3', 'R500_WTP2_R4',
#               'R500_WTP3_R1', 'R500_WTP3_R2', 'R500_WTP3_R3', 'R500_WTP3_R4',
#               'R500_WTP4_R1', 'R500_WTP4_R2', 'R500_WTP4_R3', 'R500_WTP4_R4',
#               'R500_WTP5_R1', 'R500_WTP5_R2', 'R500_WTP5_R3', 'R500_WTP5_R4',
#               'R500_WTP6_R1', 'R500_WTP6_R2', 'R500_WTP6_R3', 'R500_WTP6_R4',
#               'R500_WTP7_R1', 'R500_WTP7_R2', 'R500_WTP7_R3', 'R500_WTP7_R4']

# Select the relevant columns and calculate the average and standard deviation
TP_columns_A03 = ['A03_WTP1_R1', 'A03_WTP1_R2', 'A03_WTP1_R3', 'A03_WTP1_R4',
              'A03_WTP2_R1', 'A03_WTP2_R2', 'A03_WTP2_R3', 'A03_WTP2_R4',
              'A03_WTP3_R1', 'A03_WTP3_R2', 'A03_WTP3_R3', 'A03_WTP3_R4',
              'A03_WTP4_R1', 'A03_WTP4_R2', 'A03_WTP4_R3', 'A03_WTP4_R4',
              'A03_WTP5_R1', 'A03_WTP5_R2', 'A03_WTP5_R3', 'A03_WTP5_R4',
              'A03_WTP6_R1', 'A03_WTP6_R2', 'A03_WTP6_R3', 'A03_WTP6_R4',
              'A03_WTP7_R1', 'A03_WTP7_R2', 'A03_WTP7_R3', 'A03_WTP7_R4']

TP_columns_WO_83 = ['WO83_WTP1_R1', 'WO83_WTP1_R2', 'WO83_WTP1_R3', 'WO83_WTP1_R4',
              'WO83_WTP2_R1', 'WO83_WTP2_R2', 'WO83_WTP2_R3', 'WO83_WTP2_R4',
              'WO83_WTP3_R1', 'WO83_WTP3_R2', 'WO83_WTP3_R3', 'WO83_WTP3_R4',
              'WO83_WTP4_R1', 'WO83_WTP4_R2', 'WO83_WTP4_R3', 'WO83_WTP4_R4',
              'WO83_WTP5_R1', 'WO83_WTP5_R2', 'WO83_WTP5_R3', 'WO83_WTP5_R4',
              'WO83_WTP6_R1', 'WO83_WTP6_R2', 'WO83_WTP6_R3', 'WO83_WTP6_R4',
              'WO83_WTP7_R1', 'WO83_WTP7_R2', 'WO83_WTP7_R3', 'WO83_WTP7_R4']

avg_expression = []
std_expression = []

avg_expression_2 = []
std_expression_2 = []

avg_expression_3 = []
std_expression_3 = []

avg_expression_4 = []
std_expression_4 = []

avg_expression_5 = []
std_expression_5 = []

avg_expression_6 = []
std_expression_6 = []

for i in range(7):
    start_index = i * 4
    end_index = start_index + 4

    tp_columns = TP_columns_A03[start_index:end_index]
    tp_expression = df_filtered[tp_columns].values.flatten()
    avg_expression.append(tp_expression.mean())
    std_expression.append(tp_expression.std())
    tp_expression2 = df_filtered2[tp_columns].values.flatten()
    avg_expression_2.append(tp_expression2.mean())
    std_expression_2.append(tp_expression2.std())
    tp_expression_R = df_filtered_R5[tp_columns].values.flatten()
    avg_expression_3.append(tp_expression_R.mean())
    std_expression_3.append(tp_expression_R.std())

    tp_columns_A = TP_columns_WO_83[start_index:end_index]
    tp_expression_R2 = df_filtered_R52[tp_columns_A].values.flatten()
    avg_expression_4.append(tp_expression_R2.mean())
    std_expression_4.append(tp_expression_R2.std())
    tp_expression_A = df_filtered_A[tp_columns_A].values.flatten()
    avg_expression_5.append(tp_expression_A.mean())
    std_expression_5.append(tp_expression_A.std())
    tp_expression_A2 = df_filtered_A2[tp_columns_A].values.flatten()
    avg_expression_6.append(tp_expression_A2.mean())
    std_expression_6.append(tp_expression_A2.std())

avg_expression_list = [avg_expression, avg_expression_2, avg_expression_3, avg_expression_4, avg_expression_5, avg_expression_6]
std_expression_list = [std_expression, std_expression_2, std_expression_3, std_expression_4, std_expression_5, std_expression_6]

# create a list of colors for each gene
colors = ['blue', 'green', 'red', 'orange', 'purple', "cyan"]

# Create a new figure and axis object
fig, ax = plt.subplots()

# Iterate through each gene and plot the corresponding average expression values
for i in range(len(avg_expression_list)):
    avg_vals = avg_expression_list[i]
    std_vals = std_expression_list[i]
    
    # Plot the average expression values as a line graph, with standard deviation values represented by error bars
    ax.errorbar(TP_names, avg_vals, color = colors[i], yerr=std_vals, fmt='-o', label=gene_names[i])

# Set the axis labels
ax.set_xlabel('Time Point')
ax.set_ylabel('Expression (TPM)')

# Set the title
ax.set_title("Top 3, Bottom 3 Genes")

# Add a legend
ax.legend()

# Show the plot
plt.show()