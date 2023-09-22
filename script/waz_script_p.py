# Predictors of Weight in Romanian Infants: Weight-for-age z-scores (WAZ)
# Adrian Rus

# September 2023


# 1. Import major packages-------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats



# 2.Import the dataset-----------------------------------------------------------

# import pandas as pd

# Specify the file path
file_path = r'C:\Users\adria\Documents\waz_infants_rstudio_python\data\waz_final.csv'

# Use pandas to read the CSV file into a DataFrame
WAZdata = pd.read_csv(file_path)

# Inspect the structure of data (columns)
WAZdata.columns, WAZdata.head()



# 3. Dependent Variable (DV)-----------------------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns
# import scipy.stats as stats

## 3.1. Visual check of the DV

# Set up the matplotlib figure
plt.figure(figsize=(12, 6))

# Create subplots for histogram and boxplot
plt.subplot(1, 2, 1)
sns.histplot(WAZdata['cWageZ'], kde=True)
plt.title('Histogram of cWageZ')
plt.subplot(1, 2, 2)
sns.boxplot(x=WAZdata['cWageZ'])
plt.title('Boxplot of cWageZ')
plt.tight_layout()
plt.show() # in RStudio add this at the end of your code to explicitly show the plots

## 3.2. Compute central tendency, dispersion, skewness, kurtosis, and normality (Shapiro-Wilk P-value)

# Import the necessary packages
from scipy.stats import shapiro
from scipy import stats
import pandas as pd

# Your previous code for computing statistics (unchanged)

# Import the necessary packages
from scipy.stats import shapiro
from scipy import stats
import pandas as pd


# The code for computing statistics
count = WAZdata['cWageZ'].count()
missing = WAZdata['cWageZ'].isna().sum()
mean = WAZdata['cWageZ'].mean()
std_dev = WAZdata['cWageZ'].std()
skewness = stats.skew(WAZdata['cWageZ'])
std_error_skewness = (6 * (count - 1) / ((count - 2) * (count + 1))) ** 0.5
kurtosis = stats.kurtosis(WAZdata['cWageZ'])
std_error_kurtosis = 2 * std_error_skewness * ((count ** 2 - 1) / ((count - 3) * (count - 2)))

shapiro_p_value = shapiro(WAZdata['cWageZ'])[1]
minimum = WAZdata['cWageZ'].min()
percentile_25 = WAZdata['cWageZ'].quantile(0.25)
median = WAZdata['cWageZ'].median()
percentile_75 = WAZdata['cWageZ'].quantile(0.75)
maximum = WAZdata['cWageZ'].max()

# Create a DataFrame for the statistics table
stats_table = pd.DataFrame({
    'Statistic': ['Count', 'Missing', 'Mean', 'Standard Deviation', 'Skewness', 'Standard Error of Skewness',
                  'Kurtosis', 'Standard Error of Kurtosis', 'Shapiro-Wilk P-value', 'Minimum',
                  'Median (50th Percentile)', '75th Percentile', 'Maximum'],
    'Value': [count, missing, mean, std_dev, skewness, std_error_skewness, kurtosis,
              std_error_kurtosis, shapiro_p_value, minimum, percentile_25, median, maximum]
})

# Print the statistics table
print(stats_table)


# 4. Selection of the Independent Variables (IV)---------------------------------



