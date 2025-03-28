import requests

response = requests.get('https://google.com')

# Print out the raw HTML response content
print(response.text)