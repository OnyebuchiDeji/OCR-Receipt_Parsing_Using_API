"""
    Cleaner Way
"""

import json
import requests

image_path = "./res/"
out_path = "./ro/"
url = "https://ocr.asprise.com/api/v1/receipt"

def request_parse_receipt(imageName: str):
    res = requests.post(url,
                        data={
                        'api_key': "TEST",
                        'recognizer': 'auto',
                        'ref_no': "oct_python_123"
                        },
                        files = {
                            'file': open(image_path + imageName, 'rb')
                        }
                        )
    oname = f"response-{imageName.split(".")[0]}.json"
    with open(out_path + oname, "w") as wfs:
        """
            Either use:
                wfs.write(json.dumps(res.text, indent=4))
            OR
        """
        json.dump(json.loads(res.text), wfs, indent=4)

def read_and_display_response_info(imageName: str):
    name = f"response-{imageName.split(".")[0]}.json"
    with open(out_path + name, "r") as rfs:
        data = json.load(rfs)

    if "receipts" in data:
        receipt_info = data['receipts'][0]
        items = receipt_info['items']
        # print(items)

        print(f"Your purchase at {receipt_info['merchant_name']}")

        for item in items:
            print(f"{item['description']} - {receipt_info['currency']} {item['amount']}")

        print("-"*30)
        print(f"Subtotal: {receipt_info['subtotal']}")
        print(f"Tax: {receipt_info['tax']}")
        print("-"*30)
        print(f"Total: {receipt_info['total']}")
    else:
        print(data)

def main():
    images = ["receipt_image_3.png", "receipt_image_4.jpeg"]
    for img in images:
        request_parse_receipt(img)
        read_and_display_response_info(img)


if __name__ == "__main__":
    main()