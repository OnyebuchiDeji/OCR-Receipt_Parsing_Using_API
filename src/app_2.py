"""
    Demonstrates loading the saved response information from the API
    and seeing how the data is accessed
"""

import json


path = "./ro/"
name = "response-receipt_image_1.json"
with open(path + name, "r") as rfs:
    data = json.load(rfs)

"""
    returns a list of dictionaries --- the dictionary is the
    information from the receipt
    there is only one receipt for one received receipt information

    There is only one receipt in the response of this request, hence data['receipts'][0]
"""
# print("Receipts:\n",data['receipts'], "\n")


receipt_info = data['receipts'][0]
items = receipt_info['items']
# print(items)

print(f"Your purchase at {receipt_info['merchant_name']}\n")

for item in items:
    print(f"\t{item['description']} - {receipt_info['currency']} {item['amount']}")

print("-"*30)
print(f"Subtotal: {receipt_info['subtotal']}")
print(f"Tax: {receipt_info['tax']}")
print("-"*30)
print(f"Total: {receipt_info['total']}")