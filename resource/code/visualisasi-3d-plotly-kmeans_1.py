# visualisasi plotly

x_val = 'PURCHASES'
y_val = 'PAYMENTS'
z_val = 'BALANCE'
fig = px.scatter_3d(df_new, x=x_val, y=y_val, z=z_val, color='cluster_labels', labels='cluster_labels')
fig.show()
