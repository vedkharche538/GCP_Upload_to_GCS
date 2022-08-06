try:
    from google.cloud import storage
except ImportError:
    print("""
    Install google-cloud-storage:
    pip install google-cloud-storage
    """)
    sys.exit(1)
    """_summary_report_to_gcs.py
        Uploading file to GCS bucket
        local_filepath: local file path
        gcs_file_name: file name to be uploaded with complete path of GCS bucket
        bucket_name: GCS bucket name where file will be uploaded
    """


def upload(local_filepath: str, gcs_file_name: str, bucket_name: str):
    print("Uploading has started......")
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(gcs_file_name)
    blob.upload_from_filename(local_filepath, timeout=500)
    print("Successfully Uploaded.")
    
    
def write_file():
    client = storage.Client()
        bucket = client.get_bucket('bucket-name')
        blob = bucket.blob('path/to/new-blob-name.txt') 
        ## Use bucket.get_blob('path/to/existing-blob-name.txt') to write to existing blobs
        with blob.open(mode='w') as f:
            for line in object:
                f.write(line)
