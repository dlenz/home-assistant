import urllib3
import json
import requests

http = urllib3.PoolManager()

r = http.request('GET', 'http://video-monitoring.com/beachcams/boca/latest.json')
latest = json.loads(r.data.decode('utf-8'))
base_url = 'http://video-monitoring.com/beachcams/boca/'
img_url = latest['s4']['hr']
complete_url = base_url + img_url

with open('south_beach_latest.jpg', 'wb') as handle:
        response = requests.get(complete_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)