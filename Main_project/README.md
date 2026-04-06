This is the main instruction /explanatory file for our project. 

### Data acquisition
Data used in this project are acquired using the following sources: 
1. ERA5: please refer to GlueingData.py and HourlyToDaily.py for details on processing 
2. Temperature - produkt clima xxx 
3. Evaporation - MODIS etc xxx 

### Data smoothing
How we calculated the means and posteriors etc

to-do: Kalman filtering into the model [H] Tessa 
for daily precip/evaporation/temp
output: kalan_precip.csv

### Analysis 
The analysis (running the HBV model) is done in the notebook `HBV_varied_Su_max.ipynb`, using the script `hbv_bmi_project`.

to do: 
1. use the Kalman filtered dataset 
2. run for a longer time period (1980-2025) [done, looks good!]
    1982-2015 as calibration 
    2016-2025 as validation 
--> result: a set of optimized parameters

Doris to ask markus about soil parameter thing tmr 

Project for future scenarios: Tessa: 
per month-goes to 2080/2100 (3 scenarios) [H]
obtain temp and evaporation datasets 
-> separate Q graphs for the scenarios 


## Application to climate change 
1. Flow duration curves (confirm whather the soil is gettting flashier) Doris
2. Ea/Ep water stress index 
3. Budyko (per decade)

Challenge: get data PET (long term averages) -> Doris 

### References