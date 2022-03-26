import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "74e3f7c872554b8981649abd9dfcef81"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "francecentral"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'fr',
    'to': ['en']
}

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

def translateText(str):
    # You can pass more than one object in body.
    body = [{
        'text': str
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print(json.dumps(response))
    return response[0]['translations'][0]['text']
