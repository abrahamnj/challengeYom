import pandas as pd
import requests
from google.cloud import storage


def download_csv_from_url(url):
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    return df

def upload_csv_to_gcs(df, bucket_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    df.to_csv('resultado_web.csv', index=False)
    blob.upload_from_filename('resultado_web.csv')

def main(request):
    url = 'https://www.datos.gov.co/resource/avtd-u64r.csv'
    df = download_csv_from_url(url)
    bucket_name = 'repositorio_base_personas'
    destination_blob_name = 'your_destination_blob_name.csv'
    upload_csv_to_gcs(df, bucket_name, destination_blob_name)
    return 'CSV file uploaded to Google Cloud Storage'

