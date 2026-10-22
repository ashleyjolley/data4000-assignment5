
# Assignment 5 - Exercise 2: Inventory Reorder Analyzer

import requests

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

total_skus = 0
reorder_count = 0

while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("SKU cannot be blank.")
        continue

    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("On hand must be 0 or greater.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number.")

    total_skus += 1

    if on_hand < threshold:
        reorder_count += 1

if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

url = "https://itunes.apple.com/search"

params = {
    "entity": "song",
    "limit": 5,
    "term": term
}

songs_returned = "N/A"
api_status = "FAILED"

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    try:
        data = response.json()

        if not isinstance(data, dict):
            raise ValueError("Invalid JSON structure")

        results = data["results"]

        if not isinstance(results, list):
            raise ValueError("Results must be a list")

        if "resultCount" not in data:
            raise ValueError("Missing result count")

        if not isinstance(data["resultCount"], int):
            raise ValueError("Invalid result count")

        if data["resultCount"] != len(results):
            raise ValueError("Result count mismatch")

        count = 0

        for item in results:
            if not isinstance(item, dict):
                raise ValueError("Invalid result item")

            if "kind" not in item:
                raise ValueError("Missing kind")

            if item["kind"] == "song":
                count += 1

        songs_returned = count
        api_status = "OK"

    except (ValueError, KeyError, TypeError):
        api_status = "INVALID_RESPONSE"

except requests.exceptions.RequestException:
    api_status = "FAILED"

print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {songs_returned}")
print(f"API status: {api_status}")
