import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def process_csv(csv_file: str,output_dir:str):
    os.makedirs(output_dir,exist_ok=True)

    df = pd.read_csv(csv_file)

    json_file = os.path.join(output_dir,"netflix_titles.json")
    df.to_json(json_file,orient="records",lines=False)

def main():
    csv_file = './data/netflix_titles.csv'
    output_dir = './output_files'

    process_csv(csv_file,output_dir)

if __name__ == "__main__":
    main()