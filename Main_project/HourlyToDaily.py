### this script resampels ERA5 hourly data into daily data

from pathlib import Path
import pandas as pd

MISSING_VALUE = -9999.0


def convert_hourly_to_daily(
    input_csv: str,
    output_csv: str,
    variable_col: str,
    agg: str,
    missing_value: float = MISSING_VALUE,
) -> pd.DataFrame:
    """Convert hourly series to daily using sum (fluxes) or mean (state vars)."""
    in_path = Path(input_csv)
    if not in_path.exists():
        raise FileNotFoundError(f"Missing file: {in_path}")

    df = pd.read_csv(in_path)
    required = {"system:index", variable_col}
    if not required.issubset(df.columns):
        raise ValueError(f"{input_csv} must contain columns: {sorted(required)}")

    df["time"] = pd.to_datetime(df["system:index"].astype(str), format="%Y%m%dT%H")
    values = pd.to_numeric(df[variable_col], errors="coerce")
    values = values.where(values != missing_value)

    hourly = pd.DataFrame({"time": df["time"], variable_col: values}).set_index("time")
    hourly = hourly.sort_index()

    # Full daily index over the same covered period (expected 1980-2025).
    start_day = hourly.index.min().floor("D")
    end_day = hourly.index.max().floor("D")
    daily_index = pd.date_range(start=start_day, end=end_day, freq="D")

    if agg == "sum":
        # min_count=1 keeps days with all-missing hours as NaN for later fill to -9999.
        daily = hourly.resample("D")[variable_col].sum(min_count=1)
    elif agg == "mean":
        daily = hourly.resample("D")[variable_col].mean()
    else:
        raise ValueError("agg must be 'sum' or 'mean'")

    daily = daily.reindex(daily_index)
    missing_days = int(daily.isna().sum())
    daily = daily.fillna(missing_value)

    out_df = pd.DataFrame({
        "system:index": daily.index.strftime("%Y%m%d"),
        variable_col: daily.to_numpy(dtype=float),
    })
    out_df.to_csv(output_csv, index=False)

    print(f"Wrote {output_csv}")
    print(f"Rows: {len(out_df)} | Missing daily values filled with {missing_value}: {missing_days}")
    return out_df


if __name__ == "__main__":
    # Temperature: daily mean
    convert_hourly_to_daily(
        input_csv="ERA5_hourly_temp_1980-2025.csv",
        output_csv="ERA5_daily_temp_1980-2025.csv",
        variable_col="temperature_2m",
        agg="mean",
    )

    # Precipitation: daily sum
    convert_hourly_to_daily(
        input_csv="ERA5_hourly_precip_1980-2025.csv",
        output_csv="ERA5_daily_precip_1980-2025.csv",
        variable_col="total_precipitation_hourly",
        agg="sum",
    )

    # Evaporation: daily sum
    convert_hourly_to_daily(
        input_csv="ERA5_hourly_evap_1980-2025.csv",
        output_csv="ERA5_daily_evap_1980-2025.csv",
        variable_col="total_evaporation_hourly",
        agg="sum",
    )
