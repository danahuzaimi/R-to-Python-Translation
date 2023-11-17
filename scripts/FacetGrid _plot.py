sns.set_style("whitegrid")
sns.set_context("talk")  # Set context to "talk" for better font readability

# Create a scatterplot and a lineplot to connect the dots 
m = sns.FacetGrid(cur_data, col="Name", height=4, hue="Donor", col_wrap=5, sharex=True, sharey=True)

# Combine line and marker in a single call
m.map(plt.plot, "Concentration", "ZscoreRobust", linestyle='-', marker='o') 
m.map(plt.xticks, rotation=60, ha="right", color= "Black")
m.set_titles("{col_name}") #add title for each subplot 

# Remove inner axis titles
m.set_axis_labels('', '')  # This removes the x and y labels on all subplots

plt.suptitle("CTG data \nRobust Z-score", y=1.01)

# Add a legend for the hue (Donor) variable
m.add_legend(title="Donor", loc="upper left", bbox_to_anchor=(1.02, 1)) 
#plt.axhline(y=0, linestyle="--", color="Black")

# Add x,y text to the figure 
m.fig.text(0.5, -0.01, 'Concentration', ha='center', va='center', fontsize=30)
m.fig.text(-0.03, 0.5, 'ZscoreRobust', ha='center', va='center', rotation='vertical', fontsize=30)

plt.show()
