### To manage computation time, ERA5 Hourly data was downloaded in batches
### this script stitches the hourly data together into one csv file

from pathlib import Path
import pandas as pd

def stitch_data(
    datasets: list[str],
    variable_col: str,
    output_name: str,
    start: str = "1980-01-01 00:00:00",
    end: str = "2025-12-31 23:00:00",
    missing_value: float = -9999,
) -> pd.DataFrame:
    """Stitch multiple hourly ERA5 CSV chunks into one complete hourly time series.

    Any missing hours in the target range are filled with missing_value.
    """
    frames: list[pd.DataFrame] = []

    for dataset in datasets:
        csv_path = Path(f"{dataset}.csv")
        if not csv_path.exists():
            raise FileNotFoundError(f"Missing file: {csv_path}")

        df = pd.read_csv(csv_path)
        if "system:index" not in df.columns:
            raise ValueError(f"File {csv_path} has no 'system:index' column")
        if variable_col not in df.columns:
            raise ValueError(f"File {csv_path} has no '{variable_col}' column")

        parsed = pd.DataFrame(
            {
                "time": pd.to_datetime(df["system:index"].astype(str), format="%Y%m%dT%H"),
                variable_col: pd.to_numeric(df[variable_col], errors="coerce"),
            }
        )
        frames.append(parsed)

    stitched = pd.concat(frames, ignore_index=True)
    stitched = stitched.sort_values("time")

    # For overlapping chunks, keep the first non-null value by timestamp.
    stitched = stitched.drop_duplicates(subset=["time"], keep="first")

    full_index = pd.date_range(start=start, end=end, freq="h")
    stitched = stitched.set_index("time").reindex(full_index)
    stitched.index.name = "time"

    missing_count = int(stitched[variable_col].isna().sum())
    stitched[variable_col] = stitched[variable_col].fillna(missing_value)

    out_df = stitched.reset_index()
    out_df["system:index"] = out_df["time"].dt.strftime("%Y%m%dT%H")
    out_df = out_df[["system:index", variable_col]]
    out_df.to_csv(output_name, index=False)

    print(f"Wrote {output_name}")
    print(f"Rows: {len(out_df)} | Missing filled with {missing_value}: {missing_count}")
    return out_df


if __name__ == "__main__":
    # Temperature
    temp_datasets = [
        "Moselle_ECMWF_ERA5_LAND_HOURLY_temperature_2m_1980-01-01_2010-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_temperature_2m_2010-12-31_2011-01-01",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_temperature_2m_2011-01-01_2017-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_temperature_2m_2017-01-01_2025-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_temperature_2m_2025-12-31_2026-01-01",        
    ]
    stitch_data(
        datasets=temp_datasets,
        variable_col="temperature_2m",
        output_name="ERA5_hourly_temp_1980-2025.csv",
    )

    # Precipitation
    precip_datasets = [
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_1980-01-01_2004-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_2004-12-31_2005-01-01",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_2005-01-01_2010-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_2010-12-31_2011-01-01",
        "ERA5_total_precipitation_hourly_2011-01-01_2017-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_2017-01-01_2025-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_precipitation_hourly_2025-12-31_2026-01-01",        
    ]
    stitch_data(
        datasets=precip_datasets,
        variable_col="total_precipitation_hourly",
        output_name="ERA5_hourly_precip_1980-2025.csv",
    )

    # Evaporation
    evap_datasets = [
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_1980-01-01_2004-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_2004-12-31_2005-01-01",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_2005-01-01_2010-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_2010-12-31_2011-01-01",
        "ERA5_total_evaporation_hourly_2011-01-01_2017-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_2017-01-01_2025-12-31",
        "Moselle_ECMWF_ERA5_LAND_HOURLY_total_evaporation_hourly_2025-12-31_2026-01-01",                
    ]
    stitch_data(
        datasets=evap_datasets,
        variable_col="total_evaporation_hourly",
        output_name="ERA5_hourly_evap_1980-2025.csv",
    )
