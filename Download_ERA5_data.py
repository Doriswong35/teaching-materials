import os

with open(os.path.expanduser('~/.cdsapirc'), 'w') as f:
    f.write('url: https://cds.climate.copernicus.eu/api\n')  # new API endpoint
    f.write('key: 797aeb5c-e393-4262-8946-dca24cc5e2b7\n')  # just the key, no UID prefix needed anymore

import cdsapi
import os

c = cdsapi.Client()

os.makedirs('era5_raw', exist_ok=True)

for year in range(1980, 2025):
    outfile = f'era5_raw/era5_mosel_{year}.nc'
    
    if os.path.exists(outfile):  # skip if already downloaded
        print(f'{year} already downloaded, skipping')
        continue
    
    print(f'Downloading {year}...')
    c.retrieve(
        'reanalysis-era5-land',
        {
            'variable': [
                '2m_temperature',
                '2m_dewpoint_temperature',
                'surface_solar_radiation_downwards',
                '10m_u_component_of_wind',
                '10m_v_component_of_wind',
            ],
            'year': str(year),
            'month': [f'{m:02d}' for m in range(1, 13)],
            'day': [f'{d:02d}' for d in range(1, 32)],
            'time': '12:00',
            'area': [50.4208187527127, 5.42501288519968, 47.812500000000036, 7.850000000000015],  # N, W, S, E bounding box for Moselle basin
            'format': 'netcdf',
        },
        outfile
    )
    print(f'{year} done')
