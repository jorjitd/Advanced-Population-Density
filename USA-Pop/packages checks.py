# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:12:20 2023

@author: jorji
"""

import folium

# Create a Folium map centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add GeoJSON data with population density information
folium.Choropleth(
    geo_data=geojson_path,
    name='Population Density',
    data=gdf,
    columns=['GEOID', 'Population_Density'],
    key_on='feature.properties.GEOID',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population Density (people per square kilometer)',
).add_to(m)

# Add tooltips
style_function = lambda x: {'fillColor': 'white', 'color': 'black', 'fillOpacity': 0.1, 'weight': 0.1}
highlight_function = lambda x: {'fillColor': 'blue', 'color': 'blue', 'fillOpacity': 0.50, 'weight': 0.1}
g = folium.GeoJson(
    geojson_path,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['NAME', 'Population_Density', 'POPULATION', 'ALAND'],
        aliases=['County:', 'Population Density:', 'Population:', 'Land Area:'],
        localize=True,
    ),
)
g.add_to(m)

# Add a layer control
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('population_density_map.html')

# Display the map
m
