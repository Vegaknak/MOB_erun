
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.factorplots import interaction_plot

# Load the dataset
file_path = 'mob_dataset/MOB_testing.csv'  
data = pd.read_csv(file_path)

# Clean the data by converting 'Score' to numeric and removing NaNs
data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
data_cleaned = data.dropna(subset=['Score'])

# Calculate the mean score for each combination of participant, input mode, and orientation
data_grouped_cleaned = data_cleaned.groupby(['Participant_ID', 'Input_Mode', 'Orientation'], as_index=False).agg({'Score': 'mean'})

# Bar plot of mean scores for each combination of Input Mode and Orientation
plt.figure(figsize=(10, 6))
sns.barplot(data=data_grouped_cleaned, x='Input_Mode', y='Score', hue='Orientation', ci='sd')
plt.title('Mean Scores by Input Mode and Orientation')
plt.xlabel('Input Mode')
plt.ylabel('Mean Score')
plt.legend(title='Orientation')
plt.savefig('figures/mean_scores_plot.png')
plt.show()

# Interaction plot for Input Mode and Orientation on scores
plt.figure(figsize=(10, 6))
interaction_plot(data_grouped_cleaned['Orientation'], data_grouped_cleaned['Input_Mode'], data_grouped_cleaned['Score'],
                 colors=['red', 'blue'], markers=['D', '^'], ms=10)
plt.title('Interaction Plot: Input Mode and Orientation')
plt.xlabel('Orientation')
plt.ylabel('Mean Score')
plt.legend(title='Input Mode')
plt.savefig('figures/interaction_plot.png')
plt.show()
