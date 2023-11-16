# p1 
# Set the style of the plot
sns.set_style("whitegrid")

# Create a scatterplot and a lineplot to connect the dots 
p1 =sns.scatterplot(data=curData_pos, x="Donor_Plate", y="log10_1_Zprime", hue="Condition")
sns.lineplot(data=curData_pos, x="Donor_Plate", y="log10_1_Zprime", hue="Condition", legend= False)

# Add a title and labels 
plt.title("log10(1-Z') of data across plates and donors\nLower values represent better assay quality")
plt.xlabel("Donor_Plate")
plt.ylabel("log10(1-Z')")

# Add a horizontal dashed line at y=0
plt.axhline(0, linestyle="--", color = "Black")

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=60, ha="right")

# Show a legend to explain the colors
plt.legend(title="Condition", loc="upper left", bbox_to_anchor=(1.02, 1))

# Display the plot
plt.show(p1)

# p2
p2 = sns.scatterplot(data=curData_pos, x= "Donor_Plate", y="Zprime", hue = 'Condition')
sns.lineplot(data=curData_pos, x="Donor_Plate", y="Zprime", hue="Condition", legend= False)
plt.title("Z' of data across plates and donors\nHigher values represent better assay quality")
plt.xlabel('Donor_Plate')
plt.ylabel("Z'")
plt.axhline(0, linestyle = "--", color = "Black")
plt.xticks(rotation= 60, ha = "right")
plt.legend(title = "Condition", loc="upper left", bbox_to_anchor=(1.02,1))
plt.show(p2)
