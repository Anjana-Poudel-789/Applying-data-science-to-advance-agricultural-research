import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

# Create dataset from your research data
data = {
    'Treatment': ['Water', 'Gibberellic Acid (GA3)', 'Thiourea', 'Indole Acetic Acid (IAA)'],
    '9_DAT': [2.33, 4.67, 3.00, 2.33],
    '17_DAT': [2.50, 4.83, 3.00, 3.00],
    '28_DAT': [4.16, None, 4.67, 4.67]  # None for GA3 as it reached 80% sprouting earlier
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt the data for easier plotting
df_melted = pd.melt(df, id_vars=['Treatment'], 
                    value_vars=['9_DAT', '17_DAT', '28_DAT'],
                    var_name='Time_Point', 
                    value_name='Sprouted_Tubers')

# Clean up Time_Point labels
df_melted['Time_Point'] = df_melted['Time_Point'].str.replace('_DAT', ' DAT')

# Remove None values for plotting
df_plot = df_melted.dropna()

# Set up the plotting style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 12

# Create a comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Analysis of Potato Dormancy Breaking Treatments', fontsize=16, fontweight='bold')

# Define colors for consistent treatment representation
colors = {'Water': 'blue', 'Gibberellic Acid (GA3)': 'red', 'Thiourea': 'green', 'Indole Acetic Acid (IAA)': 'orange'}

# Plot 1: Bar chart of all treatments at 17 DAT (peak comparison)
bars = ax1.bar(df['Treatment'], df['17_DAT'], 
              color=[colors[t] for t in df['Treatment']])
ax1.set_title('Sprouted Tubers at 17 DAT', fontweight='bold')
ax1.set_ylabel('Number of Sprouted Tubers')
ax1.set_ylim(0, 6)
ax1.tick_params(axis='x', rotation=45)
# Add significance letters
ax1.text(0, df['17_DAT'][0]+0.1, 'b', ha='center', fontweight='bold')
ax1.text(1, df['17_DAT'][1]+0.1, 'a', ha='center', fontweight='bold')
ax1.text(2, df['17_DAT'][2]+0.1, 'b', ha='center', fontweight='bold')
ax1.text(3, df['17_DAT'][3]+0.1, 'b', ha='center', fontweight='bold')

# Plot 2: Line plot over time - CORRECTED
for treatment in df['Treatment']:
    treatment_data = df_melted[df_melted['Treatment'] == treatment].dropna()
    if len(treatment_data) > 0:
        # Sort by time point to ensure correct line order
        treatment_data = treatment_data.sort_values('Time_Point')
        ax2.plot(treatment_data['Time_Point'], treatment_data['Sprouted_Tubers'], 
                marker='o', markersize=8, label=treatment, color=colors[treatment])

ax2.set_title('Treatment Effects Over Time', fontweight='bold')
ax2.set_ylabel('Number of Sprouted Tubers')
ax2.set_xlabel('Days After Treatment')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Boxplot of all treatments - CORRECTED
# Since we only have one value per treatment per time point, we'll use a bar chart instead
# which is more appropriate for this data structure
time_points = ['9 DAT', '17 DAT', '28 DAT']
x = np.arange(len(time_points))
width = 0.2

for i, treatment in enumerate(df['Treatment']):
    values = []
    for time_point in time_points:
        val = df_melted[(df_melted['Treatment'] == treatment) & 
                       (df_melted['Time_Point'] == time_point)]['Sprouted_Tubers'].values
        values.append(val[0] if len(val) > 0 else np.nan)
    
    ax3.bar(x + i*width, values, width, label=treatment, color=colors[treatment])

ax3.set_title('Treatment Effects at Different Time Points', fontweight='bold')
ax3.set_ylabel('Number of Sprouted Tubers')
ax3.set_xlabel('Days After Treatment')
ax3.set_xticks(x + width * 1.5)
ax3.set_xticklabels(time_points)
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: Treatment effectiveness comparison - CORRECTED
treatment_names = ['Water', 'GA3', 'Thiourea', 'IAA']
effectiveness_17 = df['17_DAT'].values
bars = ax4.bar(treatment_names, effectiveness_17, 
              color=[colors[t] for t in df['Treatment']])
ax4.set_title('Treatment Effectiveness at 17 DAT', fontweight='bold')
ax4.set_ylabel('Number of Sprouted Tubers')
ax4.set_ylim(0, 6)
ax4.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}', ha='center', va='bottom')

# Calculate and add percentage improvement
water_control = effectiveness_17[0]
for i, (bar, treatment) in enumerate(zip(bars, treatment_names)):
    if i > 0:  # Skip the control
        improvement = (effectiveness_17[i] / water_control - 1) * 100
        ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.15,
                f'+{improvement:.1f}%', ha='center', va='bottom', color='green', fontweight='bold')

# Add significance indicators
ax4.text(0, effectiveness_17[0]+0.1, 'b', ha='center', fontweight='bold')
ax4.text(1, effectiveness_17[1]+0.1, 'a', ha='center', fontweight='bold')
ax4.text(2, effectiveness_17[2]+0.1, 'b', ha='center', fontweight='bold')
ax4.text(3, effectiveness_17[3]+0.1, 'b', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('potato_dormancy_complete_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistical analysis
print("="*60)
print("STATISTICAL ANALYSIS OF POTATO DORMANCY TREATMENTS")
print("="*60)
print("\nDescriptive Statistics:")
print(df.describe())

# Calculate treatment effectiveness
water_avg = df['17_DAT'][0]
ga3_avg = df['17_DAT'][1]
thiourea_avg = df['17_DAT'][2]
iaa_avg = df['17_DAT'][3]

print(f"\nTreatment Effectiveness at 17 DAT:")
print(f"Water (Control): {water_avg:.2f} sprouted tubers")
print(f"GA3: {ga3_avg:.2f} sprouted tubers ({((ga3_avg/water_avg-1)*100):+.1f}% improvement)")
print(f"Thiourea: {thiourea_avg:.2f} sprouted tubers ({((thiourea_avg/water_avg-1)*100):+.1f}% improvement)")
print(f"IAA: {iaa_avg:.2f} sprouted tubers ({((iaa_avg/water_avg-1)*100):+.1f}% improvement)")

# Note about statistical analysis
print("\nStatistical Analysis Note:")
print("With only one observation per treatment, formal statistical tests like ANOVA cannot be performed.")
print("The significance letters (a, b) are based on visual inspection of the data differences.")
print("For proper statistical analysis, multiple replicates per treatment would be required.")

# Create a summary table
summary_data = {
    'Treatment': df['Treatment'],
    '9_DAT': df['9_DAT'],
    '17_DAT': df['17_DAT'],
    '28_DAT': df['28_DAT'].fillna('N/A'),  # Handle None value
    'Improvement_vs_Control (%)': [
        0, 
        round((ga3_avg/water_avg-1)*100, 1), 
        round((thiourea_avg/water_avg-1)*100, 1), 
        round((iaa_avg/water_avg-1)*100, 1)
    ]
}

summary_df = pd.DataFrame(summary_data)

print("\nSummary Table:")
print(summary_df.to_string(index=False))

print("\nKey Findings:")
print("- GA3 showed the highest effectiveness (93.2% improvement vs control)")
print("- Thiourea and IAA showed moderate effectiveness (20% improvement)")
print("- GA3 treatment reached 80% sprouting earlier than other treatments")
print("- Results demonstrate GA3's potential for optimizing potato planting schedules")

print("\nLimitations:")
print("- This analysis is based on single observations per treatment")
print("- Future studies should include multiple replicates for statistical testing")
print("- More time points would provide better understanding of treatment dynamics")

print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)