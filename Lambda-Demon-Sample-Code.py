
import requests

url = "https://www.amazon.com"

def handler(event, context):
    try:
        response = requests.get(url)
        # Return the status code of the response
        return response.status_code
    except requests.exceptions.RequestException as e:
        # Return an exception if there is an error in the request
        return str(e)