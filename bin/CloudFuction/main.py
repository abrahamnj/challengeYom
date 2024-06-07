# from google.cloud import storage
# import requests

# def main(request):
#     url = 'https://www.datos.gov.co/resource/avtd-u64r.csv'
#     response = requests.get(url)

#     # Guarda el archivo en el bucket
#     bucket_name = "repositorio_base_personas"
#     blob_name = "data.csv"
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(blob_name)
#     blob.upload_from_string(response.content.decode("utf-8"))

#     return f"Archivo {blob_name} subido exitosamente al bucket {bucket_name}"

from google.cloud import storage
import requests
import zipfile

def main(request):
    url = 'https://www.datos.gov.co/resource/avtd-u64r.csv'
    response = requests.get(url)

    # Guarda el archivo en el bucket
    bucket_name = "repositorio_base_personas"
    blob_name = "base_descargada_web.csv"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(response.content.decode("utf-8"))

    # Agregar la parte de código para empaquetar "main.py" en un archivo ZIP llamado "function_code.zip"
    zip_filename = "function-code.zip"
    python_filename = "main.py"
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        zip_file.write(python_filename)

    return f"Archivo {blob_name} subido exitosamente al bucket {bucket_name} y {python_filename} empaquetado en {zip_filename}"
