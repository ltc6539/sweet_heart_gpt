from googleapiclient.discovery import build

def get_google_customsearch_service(api_key):
    return build('customsearch', 'v1',developerKey=api_key)
