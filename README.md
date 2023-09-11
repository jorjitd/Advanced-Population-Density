# Population Density Map

This project creates an interactive population density map for US counties using open data from the US Census Bureau. It allows you to visualize population density at the county level and provides population information on hover.


## Getting Started

Follow these instructions to set up and run the project on your local machine. 

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/population-density-map.git
   cd population-density-map

###  Install the required Python libraries:

    ```bash
    pip install geopandas plotly folium



Usage
Download the open data:

US Counties Shapefile Data
County-Level Population Data
Prepare the data:

Place the US Counties Shapefile data in the data/ directory as us_counties_shapefile.shp.
Place the County-Level Population Data in the data/ directory as county_population_data.csv.
Run the Python script to create the population density map:

bash
Copy code
python create_population_density_map.py
The map will be generated and displayed. You can interact with it, zoom in/out, and hover over counties to view population information.

To save the Folium-based map as an HTML file, check the population_density_map.html file in the project directory.

Customize
You can customize the project by:

Changing the data sources to visualize population density for a different region.
Modifying the color schemes and legends in the code for better visualization.
Adding more tooltips or information to be displayed on hover.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
US Census Bureau for providing the open data.
GeoPandas for geospatial data handling.
Plotly for creating interactive visualizations.
Folium for interactive leaflet maps.
Feel free to contribute to this project by opening issues or pull requests!
