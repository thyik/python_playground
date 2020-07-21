import json
import os

import urllib3
from urllib.parse import urlparse
import httplib2 as http  # External library

if __name__ == "__main__":
    # Authentication parameters
    acct_key = os.getenv('LTA_DATAMALL_KEY')
    headers = {'AccountKey': acct_key, 'accept': 'application/json'}  # this is by default

    # API parameters
    uri = 'http://datamall2.mytransport.sg'
    # Resource URL
    path = '/ltaodataservice/BusArrivalv2?BusStopCode=83139'

    # Build query string & specify type of API call
    target = urlparse(uri + path)
    print(target.geturl())

    method = 'GET'
    body = ''
    # Get handle to http
    h = http.Http()

    # Obtain results
    response, content = h.request(target.geturl(), method, body, headers)
    # Parse JSON to print
    jsonObj = json.loads(content)
    print(json.dumps(jsonObj, sort_keys=True, indent=4))

    # Save result to file
    with open("bus_routes.json", "w") as outfile:
        # Saving jsonObj["d"]
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
