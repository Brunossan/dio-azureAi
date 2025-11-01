import os
import azure.storage.blob as azure_blob
import streamlit as st
from utils.config import config

BlobServiceClient = azure_blob.BlobServiceClient

def upload_file_to_blob(file, file_name):
    try:
        
        blob_service_client = BlobServiceClient.from_connection_string(config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(bcontainer=config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)

        return blob_client.url
    except Exception as e:
        st.error(f"An error occurred while uploading to Blob Storage: {e}")
        return None
