import plotly.express as px

# Load the GeoJSON file for Plotly visualization
geojson_path = "county_population.geojson"

# Create an interactive map using Plotly
fig = px.choropleth(
    geojson=geojson_path,
    locations='GEOID',
    featureidkey="properties.GEOID",
    color='Population_Density',
    hover_name='NAME',
    hover_data=['POPULATION', 'ALAND'],
    title='US County Population Density Map',
    color_continuous_scale='YlOrRd',
    projection='mercator'
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(autosize=True)

# Show the map
fig.show()
