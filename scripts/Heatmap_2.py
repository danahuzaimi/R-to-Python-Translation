# Create two pivot tables that are exactly the same, except for their values. 
# One is for the 'values' and the other is for 'annotations'.
def prepare_data_for_heatmap(df):
    return (df.pivot_table(index='Row', columns='Column', values='NormBg', aggfunc='mean'), # Values
            df.pivot_table(index='Row', columns='Column', values='Group', aggfunc='first')) # Annotation

# Using FacetGrid for multiple heatmaps
g = sns.FacetGrid(curData, col="Donor", row="Plate", margin_titles=True, despine=False, sharex=False, sharey=False, height=10)

# Drawing the heatmap for each facet
def draw_heatmap(*args, **kwargs):
    data = kwargs.pop('data')
    values, annotations = prepare_data_for_heatmap(data)
    sns.heatmap(values, annot=annotations, fmt='s', **kwargs, annot_kws={"size": 10, "ha":"center", "va":"center"}) 
g.map_dataframe(draw_heatmap, cmap="coolwarm", cbar=False)
                
#Adjusting the aesthetics
g.set_axis_labels("Column", "Row")
g.fig.subplots_adjust(right=0.9)
cbar_ax = g.fig.add_axes([0.92, .3, .02, .4])  # Create an axis for the colorbar
g.figure.colorbar(g.axes[0, 0].collections[0], cax=cbar_ax)
g.fig.suptitle("Background corrected cell number in data", size=16, y=1.05)

# Adjust font size
sns.set(font_scale=0.8)

# Show the plot
plt.show()
