# ENVM1502 Project Poster journal - directory
*Tessa Wallier, Doris Wong*

This is a directory of all files submitted as part of the poster journal, which explains where to find code for each part of our project. Please refer to individual notebooks for more notes on the methodology and results. 

### Data acquisition
Temperature, precipitation and evaporation data used in this project are acquired from ERA5, covering years 1980-2025. `GlueingData.py` and `HourlyToDaily.py` are scripts used to concactenate data download in batches and convert hourly data to daily data. Discharge data is obtained from the GRDC dataset, station 6336500 `6336500_Q_Day.Cmd.txt`. 

Kalman filtering for precipitation was carried out using additional data from CHIRPS in `Daily_Kalman_smoothing.ipynb`. However, it was not used in the analysis as we could not find alternative datasets at the same resolution for a sufficiently meaningful overlapping period for the other variables. This notebook also contained initial processing for predictions of the variables from climate models, which were not used in the end. 

### Analysis 
There are two possible pathways through which warming could influece discharge: ...


For analysis on Su_max:

The analysis (running the HBV model) is done in the notebook `HBV_varied_Su_max.ipynb`, using the script `hbv_bmi_project`. Resuls of the MC calibration are stored in `results_mc_slow.csv`. 

For analysis on actual evapotranspiration: 

`AET_temperature_analysis.ipynb` and  `hbv_et_temperature_analysis.ipynb`

### References
Davidson, E. and Janssens, I. A. (2006). Temperature sensitivity of soil carbon decomposition and feedbacks to climate change. Nature 440, 165–173 (2006). https://doi.org/10.1038/nature04514

Ma, R., Kou, T., Cheng, X. and Yu, N. (2024). Long-term warming altered soil physical structure and soil organic carbon pools in wheatland field. Experimental Agriculture, 60, e1. https://doi.org/10.1017/S0014479723000236

Stocker, B. D., Tumber-Dávila, S. J., Konings, A. G., Anderson, M. C., Hain, C. and Jackson, R. B. (2023). Global patterns of water storage in the rooting zones of vegetation. Nature Geoscience, 16(3), 250–256. https://doi.org/10.1038/s41561-023-01125-2

Oishy, M. N., Shemonty, N. A., Fatema, S. I., Mahbub, S., Mim, E. L., Raisa, M. B. H. and Anik, A. H. (2025). Unravelling the effects of climate change on the soil-plant-atmosphere interactions: A critical review. Soil & Environmental Health, 3(1), 100130. https://www.sciencedirect.com/science/article/pii/S2949919425000032

Pham, T. A., Hashemi, A., Sutman, M. and Medero, G. M. (2023). Effect of temperature on the soil–water retention characteristics in unsaturated soils: Analytical and experimental approaches. Journal of Hydrology, 620, 129431. https://doi.org/10.1016/j.sandf.2023.101301 