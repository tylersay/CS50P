import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

URL = "https://itunes.apple.com/search?entity=song&limit=1&term="
response = requests.get(URL + sys.argv[1])

print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])