# OpenStreetMap Amenities

Authors: Patrick Erismann, Olga Voll, Gérôme Meyer  
This is a project made in the context of the PM3 module.

## Installation with Docker
This project is dependent on docker to run. It can be started by running the docker-compose command in
the root of the project directory.

```bash
docker-compose up
# Add the flag -d to start in the background.
```

### Adding new dependencies
In order to add a new dependency / library it needs to be added to the `requirements.txt`.
The image will need to be re-built after adding the requirement. 
```bash
docker-compose build
```

## Libraries
Python dependencies are listed in the `src/requirements.txt` and are automatically installed with `pip install` in
the python container. Only `flask` and `pymongo` were used.  
All JavaScript libraries were manually downloaded and are located in the `src/static/lib/` directory.

### Leaflet
Leaflet is the leading open source JavaScript library for mobile-friendly interactive maps.  The library 
was used to create the map of Switzerland and provide a better visual representation of ATM. 
Using the library's capabilities, markers could be used to place all existing ATMs of the bank selected 
in the chart on the map.

### MUI
Material UI (MUI is a comprehensive collection of pre-built components ready for immediate use in 
production. This framework has been used to design interface. 

### Chart
The Chart.js library enables graphical visualisations of the data for the applications. In this case, 
the ATM statistics were visualised by operator, as well as by the canton. The data was displayed sorted. 
For the analysis, the data was used in JSON format. 

### SeedRandom
The seedRandom.js library by David Bau is used to generate random colors for each canton bar chart while 
ensuring that these random colors are always the same for the same canton.

## Data
The processed data are placed in the folder "src/data", as well as the file with the code of the processing.  
The given OpenStreetMap dataset was filtered to only include "ATM" amenities. 

Additionally, the data was preprocessed and then stored in the `clean_data.json` file, which is passed on to Mongo 
database upon start-up. 

### Project directory structure
```
├── docker-compose.yml
├── README.md
└── src
    ├── data
    ├── database_handler.py
    ├── Dockerfile
    ├── requirements.txt
    ├── server.py
    ├── static
    │   ├── css
    │   ├── images
    │   ├── js
    │   ├── lib
    │   └── logos
    └── templates
```
