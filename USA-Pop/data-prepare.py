import geopandas as gpd
import pandas as pd

# Load the shapefile data for US counties
shapefile_path = 'path/to/us_counties_shapefile.shp'
gdf = gpd.read_file(shapefile_path)

# Load population data at the county level (adjust the file path)
population_data_path = 'path/to/county_population_data.csv'
pop_data = pd.read_csv(population_data_path)

# Merge the population data with the shapefile data
gdf = gdf.merge(pop_data, left_on='GEOID', right_on='FIPS')

# Calculate population density
gdf['Population_Density'] = gdf['POPULATION'] / (gdf['ALAND'] / 1e6)  # Convert land area to square kilometers

# Create a GeoJSON file for Plotly visualization
gdf.to_file("county_population.geojson", driver='GeoJSON')
