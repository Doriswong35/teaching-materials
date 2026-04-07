This is the main instruction /explanatory file for our project. 

### Data acquisition
Data used in this project are acquired using the following sources: 
1. ERA5: please refer to GlueingData.py and HourlyToDaily.py for details on processing 
2. Temperature - produkt clima xxx 
3. Evaporation - MODIS etc xxx 

### Data smoothing
How we calculated the means and posteriors etc

### Analysis 
The analysis (running the HBV model) is done in the notebook `HBV_varied_Su_max.ipynb`, using the script `hbv_bmi_project`.

to do: 
1. use the Kalman filtered dataset (only precipitation)
2. run for a longer time period (1980-2025) [done, looks good!]
    1982-2015 as calibration 
    2016-2025 as validation 
--> result: a set of optimized parameters

Project for future scenarios: Tessa: 
per month-goes to 2080/2100 (3 scenarios) [H]
obtain temp and evaporation datasets 
-> separate Q graphs for the scenarios 

## Drawing conclusions
hyporhesis testing for linear relationship between temp and Ea/P (maybe conclude that temperature has a much stronger influence on Ea/P than Su_max?)

### References