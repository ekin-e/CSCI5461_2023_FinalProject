import pandas as pd
import matplotlib.pyplot as plt

predicted_col = "Predicted Value" 
original_col = "Original value"

diff_threshold = 3

df = pd.read_csv("predicted_values_rf.csv")
df2 = pd.read_csv("predicted_values_svr_Linear.csv")
df3 = pd.read_csv("predicted_values_svr_rbf.csv")
df4 = pd.read_csv("predicted_values_xgb.csv")
df5 = pd.read_csv("predicted_values_ridge_01.csv")
df6 = pd.read_csv("predicted_values_ridge_05.csv")
df7 = pd.read_csv("predicted_values_ridge_1.csv")
df8 = pd.read_csv("predicted_values_ridge_5.csv")
df9 = pd.read_csv("predicted_values_ridge_10.csv")
df10 = pd.read_csv("predicted_values_ridge_30.csv")


count_rf = len(df[(abs(df[predicted_col] - df[original_col]) <= diff_threshold)])
count_svr_l = len(df2[(abs(df2[predicted_col] - df2[original_col]) <= diff_threshold)])
count_svr_rbf = len(df3[(abs(df[predicted_col] - df3[original_col]) <= diff_threshold)])
count_xgb = len(df4[(abs(df4[predicted_col] - df4[original_col]) <= diff_threshold)])
count_r01 = len(df5[(abs(df5[predicted_col] - df5[original_col]) <= diff_threshold)])
count_r05 = len(df6[(abs(df6[predicted_col] - df6[original_col]) <= diff_threshold)])
count_r1 = len(df7[(abs(df7[predicted_col] - df7[original_col]) <= diff_threshold)])
count_r5 = len(df8[(abs(df8[predicted_col] - df8[original_col]) <= diff_threshold)])
count_r10 = len(df9[(abs(df9[predicted_col] - df9[original_col]) <= diff_threshold)])
count_r30 = len(df10[(abs(df10[predicted_col] - df10[original_col]) <= diff_threshold)])

print(f"RF Number of genes with a difference of {diff_threshold}: {count_rf}")
print(f"SVR Linear Number of genes with a difference of {diff_threshold}: {count_svr_l}")
print(f"SVR RBF Number of genes with a difference of {diff_threshold}: {count_svr_rbf}")
print(f"XGB Number of genes with a difference of {diff_threshold}: {count_xgb}")
print(f"Ridge01 Number of genes with a difference of {diff_threshold}: {count_r01}")
print(f"Ridge05 Number of genes with a difference of {diff_threshold}: {count_r05}")
print(f"Ridge1 Number of genes with a difference of {diff_threshold}: {count_r1}")
print(f"Ridge5 Number of genes with a difference of {diff_threshold}: {count_r5}")
print(f"Ridge10 Number of genes with a difference of {diff_threshold}: {count_r10}")
print(f"Ridge30 Number of genes with a difference of {diff_threshold}: {count_r30}")

# Plotting

# Create a dictionary of counts
counts = {
    "RF": count_rf,
    "SVR Linear": count_svr_l,
    "SVR RBF": count_svr_rbf,
    "XGB": count_xgb,
    "Ridge": count_r5,
}

# Create a bar plot
plt.bar(range(len(counts)), list(counts.values()), align='center')
plt.xticks(range(len(counts)), list(counts.keys()))
plt.xlabel("Models")
plt.ylabel("Number of genes with a prediction difference of 3")
plt.title("Comparison of models (original phase vs predicted phase)")
plt.show()