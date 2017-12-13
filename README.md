# iNaturalist SDM

## Basic Overview

This application provides a full data pipeline for getting and cleaning iNaturalist and ebutterfly butterfly data, and running this data through Jeff Oliver's species distribution models and algorithms, which creates rasters and image files that help scientists visualize how different butterfly species are distributed across the country, given the month of the year, as well as a stacked image to see the total distribution of butterflies in North America.

# VIS TEAM ***********************************************************************************
![input output](https://github.com/ckhoward/iNat-SDM/blob/master/imgs/inputoutput.jpg?raw=true "Input to output")

## System Requirements:
    Software: Python 3.6, R, Git, Anaconda(install as Admin), Bash on Ubuntu
    R packages: dismo, sp, raster, maptools, rgdal, gtools

[Install Ubuntu Bash on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/install-win10)

[Install R on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-16-04-2)

Install R Packages by typing the following commands into Bash and pressing 'enter' after each:
1. R
2. install.packages('rgdal')
3. install packages('sp')
4. install.packages('maptools')
5. install.packages('dismo')
6. install.packages('raster')
7. install.packages('gtools')
    



## Getting started:

1. Clone the required projects
 * Get Jeff Oliver's SDM with the command ```git clone https://github.com/jcoliver/ebutterfly-sdm.git```
 * Get this program with with the command ```git clone https://github.com/acic2017/Butterfly-SDM.git```
 * Then change directories into the above with the command ```cd Butterfly-SDM```

2. Get your data
To Download iNaturalist data:
 * If downloading [GBIF Observations](http://www.inaturalist.org/observations/gbif-observations-dwca.zip), unzip the downloaded file, and move observations.csv into the directory with organize.py (warning: many input files will be generated here)
To Download eButterfly data:
* Download [eButterfly Data Dump](https://de.cyverse.org/dl/d/BA2D5507-1F85-4A75-8F11-5B537E44A2D9/ebutterfly-acic.sql), use the SQL to csv file, and move the csv (in this case eb_butterflies_new.csv) into the directory with organize.py 

3. Organize your files
 * ?????
 * Where the organize.py, observations.csv, and eb_butterflies_new.csv are located will create an output file for each species of butterfly that is cleaned through the organize.py file and will have a large folder count (DO NOT PLACE ON DESKTOP)


## How to use:
Run organize.py with ```python organize.py``` from the command line. This script:
 * Cleans the observations.csv and eb_butterflies_new.csv data by removing extraneous and/or missing data ;
 * Creates a user-friendly file, data_for_sdm.csv, containing all observations, with data for Scientific Name, year, month, latitude, and longitude. A text copy is able to be created too, just in case it is preferred. This makes it easier for users to sift through the data of interest, to find any glaring issues;
 * Creates a csv for every species listed in data_for_sdm.csv, that is located in North America, and has a minimum of 13 observations, one for each month, and one for all months, to be used as input for the SDM, as the format [scientific_name_month.csv].


# JUPYPTER NOTEBOOK INFO


## Input:

Apart from species map and raster files, the Jupyter Notebook uses user inputs to select a species by scientific name, algorithm to use, and prediction level of interest. The selected species will have its outputs provided as cells are executed.

## Output:

The output shows the expected SDM along with 9 possible animations of the species' SDMs over all the months for each algorithm/prediction threshold combination.

# Vis teams image display*******************************************************************
![Species Distributions](https://github.com/acic2017/Butterfly-SDM/blob/master/gifs/Papilio_glaucus-CTA-1.gif?raw=true "January through December and All")



## Warnings

#### Data integrity:

The data_for_sdm.csv that is created contains ALL Lepidoptera observations with valid inputs from both databases, worldwide, regardless of number of observations. The final output is put through a series of filters to ensure only North American species and a minimum number of observations (13) is obtained. This was done to allow researchers the ability to access a clean, combined version of the observations, and be used on any number of unforeseen future analysis

In order to remove or change these filters, for example, to include ALL observations not just those from North America or ones that are less that the 13 observations per species threshold, organize.py may be altered; see the file itself for more detailed instructions.

#### Runtimes:

Approximate run time for organization.py to clean and organize/write needed files for the SDM : ~45minutes (data_for_sdm.csv is veiwable after ~5 minutes)

# COMPUTATION TEAM***************************************************************************************************
Approximate run time for SDM/R Script to fully run 5 Taxon ID's and recieve Raster Images: ~3minutes
Estimated run time for SDM/R Script to fully run all 760-780 Taxon ID's and recieve Raster Images: ~6.5hours


#### Space requirement:

# COMPUTATION TEAM/VIS TEAM****************************************************************************************


## License

This program is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contribution

Have an issue? The repository is currently public, but this may change in the future. If you suddenly find that you do not have access to make alterations, file an issue and we will quickly respond. 


 
#### Contributors


Eric Tsetsi, Phillip Johnson, Jorge Barrios, Chris Howard
Janice Walsh, Adrianna Salazar, Asa Myrvik, Megha Agarwal
Jasmin Khan Niazi, Daniel Phillips, Jeremiah Hanson
Isaiah Hanson, Ryan Watson, Sina Ehsani
 
 







