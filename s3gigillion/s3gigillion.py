from boto3 import client

SERVICE_ENDPOINT = 'https://s3.gigillion.com'

def get_client(access_key_id,
               secret_access_key,
               session_token=None):

    storage = _GigillionStorage(access_key_id, secret_access_key, session_token).storage
    return storage

class _GigillionStorage:

    def __init__(self,
                 access_key_id,
                 secret_access_key,
                 session_token=None):
        self.storage = client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
            endpoint_url=SERVICE_ENDPOINT
        )
