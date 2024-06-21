
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import mixedlm

# Load the dataset
file_path = 'mob_dataset/MOB_testing.csv' 
data = pd.read_csv(file_path)

# Clean the data by converting 'Score' to numeric and removing NaNs
data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
data_cleaned = data.dropna(subset=['Score'])

# Calculate the mean score for each combination of participant, input mode, and orientation
data_grouped_cleaned = data_cleaned.groupby(['Participant_ID', 'Input_Mode', 'Orientation'], as_index=False).agg({'Score': 'mean'})

# Run mixed-design ANOVA using a mixed linear model
model_cleaned = mixedlm("Score ~ Input_Mode * Orientation", data_grouped_cleaned, groups=data_grouped_cleaned["Participant_ID"])
result_cleaned = model_cleaned.fit()

# Display the results
anova_summary = result_cleaned.summary()
print(anova_summary)

# Save the ANOVA summary to a text file
with open('anova_summary.txt', 'w') as file:
    file.write(anova_summary.as_text())
