# backend_server_template
Simple template for a back-end service using Tornado.

This is just a simple template for building a back-end service to run,
for example, on an EC2 instance.

You can test it locally, e.gg, using Postman or Python:

```import requests
import json
import requests

url = "http://localhost:8001/api_endpoint?key=123"

payload = json.dumps({
  "body_key": "my body"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

