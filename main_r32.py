from scipy import stats

# Sample data
data1 = [1.1, 2.2, 3.3, 4.4, 5.5]
data2 = [2.1, 3.2, 4.3, 5.4, 6.5]

# Perform an independent t-test
t_statistic, p_value = stats.ttest_ind(data1, data2)

# Print the t-statistic and p-value
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
