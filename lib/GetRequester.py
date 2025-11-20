import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self): 
        self.response = requests.get(self.url)
        return self.response.content

    def load_json(self):
        self.get_response_body()
        formatted = self.response.json()
        print(formatted)
        return formatted

requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

requester.get_response_body()
requester.load_json()