# Get unique values from the 'Compound_Annot' column in the 'curData' DataFrame
samples = curData['Compound_Annot'].unique()

# Create a list 'rmSamples' containing names of samples to be removed
rmSamples = ["Media_NA", "DMSO_NA", "Cells_NA", "P_NA", "C_NA", "A_NA"]

#remove rmSamples from samples
samples = list(set(samples) - set(rmSamples))
cur_data = curData[curData['Compound_Annot'].isin(samples)].copy()
cur_data['Name'] = cur_data['TARGET_ID'] + '\n' + cur_data['Compound_Annot']

# Create a new column 'Donor_Dose' by combining 'Donor' and 'Concentration' columns
cur_data['Donor_Dose'] = cur_data['Donor'] + '_' + cur_data['Concentration']
cur_data1 = cur_data[['Compound_Annot', 'Plate', 'Donor_Dose', 'NormDMSO']]
cur_data1 = cur_data.pivot(index='Compound_Annot', columns='Donor_Dose', values='NormDMSO')

# Remove 'Plate' column and select columns from the 3rd to the last
# Get the minimum and maximum values
min_val = cur_data1.values.min()
max_val = cur_data1.values.max()

# Set up the heatmap
plt.figure(figsize=(7, 15))
sns.heatmap(
    data=cur_data1,
    cmap="Blues",
    cbar=True,
    yticklabels= True,
    annot=True,
    annot_kws={"size": 10},
    fmt=".2f",
    linewidths=0.5,
    linecolor='grey',
    cbar_kws={"label": "DMSO Normalized"})

plt.title("DMSO Normalized Values in AlphaLISA Data")
plt.xlabel("Donor_Dose")
plt.show()
