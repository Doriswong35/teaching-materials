This is the main instruction /explanatory file for our project. 

### Data acquisition
Data used in this project are acquired from ERA5. Kalman filtering for precipitation was carried out using additional data from CHIRPS in `Daily_Kalman_smoothing.ipynb`. However, it was not used in the analysis as we could not find alternative datasets at the same resolution for a sufficiently meaningful overlapping period for the other variables. This notebook also contained initial processing for predictions of the variables from climate models, which were not used in the end. 

### Analysis 
For Su_max:

The analysis (running the HBV model) is done in the notebook `HBV_varied_Su_max.ipynb`, using the script `hbv_bmi_project`.

For actual ecapotranspiration: 

`hbv_et_temperature_analysis.ipynb`

### References
