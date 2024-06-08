from google.cloud import storage
import requests

def gatillador(request):
    """
    Esta función descarga un archivo CSV desde una URL y lo sube a un bucket de Google Cloud Storage.
    :param request: No se utiliza en el código.
    :return: Mensaje indicando que el archivo se ha subido correctamente al bucket.
    """
    url = 'https://www.datos.gov.co/resource/avtd-u64r.csv'
    response = requests.get(url)

    # Guarda el archivo en el bucket
    bucket_name = "repositorio_base_personas"
    blob_name = "base_descargada_web.csv"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(response.content.decode("utf-8"))

    return f"Archivo {blob_name} subido exitosamente al bucket {bucket_name}"
