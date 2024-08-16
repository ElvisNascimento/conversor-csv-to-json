import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import streamlit as st

def process_csv(csv_file: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_file)
    json_file = os.path.join(output_dir, "netflix_titles.json")
    df.to_json(json_file, orient="records", lines=False)
    return json_file

def main():
    st.title("CSV to JSON Converter")

    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    output_dir = "output_files"

    if csv_file is not None:
        json_file = process_csv(csv_file, output_dir)
        st.success(f"JSON file has been created: {json_file}")

        st.download_button(
            label="Download JSON file",
            data=open(json_file, 'r').read(),
            file_name="netflix_titles.json",
            mime="application/json"
        )
if __name__ == "__main__":
    main()