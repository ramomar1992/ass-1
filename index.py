from pandas import read_csv
import numpy as np

# Open the csv as a data frame in python using the pandas package. Inspect the data frame to get an idea of the metrics reported and the format of the table.
table = read_csv("phi_data.csv")
print(table)

# Create a list that contains the following elements: Type, Filter, TRUTH.TP, TRUTH.FN, QUERY.FP, METRIC.Precision.
subset = ["Type", "Filter", "TRUTH.TP", "TRUTH.FN", "QUERY.FP", "METRIC.Precision"]

# Use the list to subset the data frame and keep the desired columns.
subset_table = table[subset]

# Create two numpy arrays, one with the TRUTH.TP numbers and another with the QUERY.FP numbers
true_pos = np.array(subset_table["TRUTH.TP"])
false_pos = np.array(subset_table["QUERY.FP"])

# Calculate precision using your numpy arrays. Hint: Precision = True Positives / (True Positives + False Positives)
precision = true_pos / (true_pos + false_pos)

#Compare your values to the values in “METRIC.Precision”
compare = abs(precision - subset_table["METRIC.Precision"])
print(compare)

"""_summary_
0    0.000556
1    0.000785
2    0.000008
3    0.000001
"""

# Provide your python script, and precision values to 2 decimal places for INDEL ALL variants, INDEL PASS variants, SNP ALL variants and SNP PASS variants.
type_filter_precision = subset_table[["Type", "Filter"]]
type_filter_precision["Precision"] = precision.round(2)
print(type_filter_precision)

"""_summary_
    Type Filter  Precision
0  INDEL    ALL       0.96
1  INDEL   PASS       0.96
2    SNP    ALL       0.99
3    SNP   PASS       1.00
"""
