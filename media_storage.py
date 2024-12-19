from minio import Minio
import hashlib
from config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, TEMPLATE_IMAGE_FILENAME_GET, BUCKET_NAME


client = Minio(MINIO_ENDPOINT, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY, secure=False)

def fileHash(filename:str):
    return hashlib.md5(open(filename,'rb').read()).hexdigest()


#todo: put used hashes into key-value db
def save_file(filename:str) -> str:
    file_extension = filename.split(".")[-1]
    filename_of_savedFile = fileHash(filename) + '.' + file_extension
    client.fput_object(BUCKET_NAME, filename_of_savedFile, filename)
    return filename_of_savedFile
    
def get_file(filename:str):
    client.fget_object(BUCKET_NAME, filename, TEMPLATE_IMAGE_FILENAME_GET)
    return TEMPLATE_IMAGE_FILENAME_GET
