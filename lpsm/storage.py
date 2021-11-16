from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob - bucket.blob(destination_blob_name)
    blob.upload_from_file(source_file_name)

def get_pic(bucket_name, filename):
    storage_client = storage.Client()
    bucket = storage_client(bucket_name)
    blob = bucket.blob(filename)
    return blob.public_url

def file_in_storage(bucket_name, filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    return blob.exists()