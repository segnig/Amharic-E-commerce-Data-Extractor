import json
import csv

def save_to_json(data, filename):
    """
    Saves the given data to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename):
    """
    Saves the given data to a CSV file.
    """
    if not data:
        print("No data to save.")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}") 