"""
    Demonstrates sending th eimage to the api to obtain the information parsed from the image
"""

import json
import requests


url = "https://ocr.asprise.com/api/v1/receipt"

image = "./res/receipt_image_2.jpg"

"""
    Concerning the API_KEY, one can use the 'TEST' key
    but this is limited.

    But an account can also be created to allow better access privileges

    Consider that the `file` keyword is the payload in bytes
"""
res = requests.post(url,
                    data={
                        'api_key': "TEST",
                        'recognizer': 'auto',
                        'ref_no': "oct_python_123"
                    },
                    files = {
                        'file': open(image, 'rb')
                    }
                    )
"""
    It is important to do `json.loads(res.text)` to parse the returned text as json format
    so that json.dump()'s output removes unnecessary characters and properly displays data.
    `response-receipt_image_1_v2.json` shows what happens when this is not the case.
"""
path = "./ro/"
with open(path + "response-receipt_image_2.json", "w") as wfs:
    """
        Either use:
            wfs.write(json.dumps(res.text, indent=4))
        OR
    """
    json.dump(json.loads(res.text), wfs, indent=4)