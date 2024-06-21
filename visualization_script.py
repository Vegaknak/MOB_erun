import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.factorplots import interaction_plot

# Load the dataset
file_path = 'MOB_testing.csv'  
data = pd.read_csv(file_path)

# Clean the data by converting 'Score' to numeric and removing NaNs
data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
data_cleaned = data.dropna(subset=['Score'])

# Calculate the mean score for each combination of participant, input mode, and orientation
data_grouped_cleaned = data_cleaned.groupby(['Participant_ID', 'Input_Mode', 'Orientation'], as_index=False).agg({'Score': 'mean'})

plt.figure(figsize=(6, 8))  # Adjusted figure size for a narrower plot
bar_plot = sns.barplot(data=data_grouped_cleaned, x='Input_Mode', y='Score', hue='Orientation',
            palette=['#29274C', '#B49FCC'], ci='sd', width=0.4, zorder=3)  
plt.title('Mean Scores by Input Mode and Orientation')
plt.xlabel('Input Mode')
plt.ylabel('Mean Score')
plt.legend(title='Orientation')

plt.grid(True, linestyle='--', linewidth='0.5', color='grey', alpha=0.4, axis='y', zorder=1)  # Lower zorder for grid lines
#plt.savefig('figures/mean_scores_plot.png')
plt.show()


# Interaction plot for Input Mode and Orientation on scores
plt.figure(figsize=(8, 4))
interaction_plot(data_grouped_cleaned['Orientation'], data_grouped_cleaned['Input_Mode'], data_grouped_cleaned['Score'],
                 colors=['#29274C', '#B49FCC'], ms=10)
plt.title('Interaction Plot: Input Mode and Orientation')
plt.xlabel('Orientation')
plt.ylabel('Mean Score')
plt.legend(title='Input Mode')
plt.grid(True, linestyle='--', linewidth='0.5', color='grey', alpha=0.5, axis='y', zorder=0)  
#plt.savefig('figures/interaction_plot.png')
plt.show()
