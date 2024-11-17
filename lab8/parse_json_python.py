#!/usr/local/bin/python3.12

import json
import csv

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for repo in data[:5]:  # Limit to first 5
        name = repo.get('name', '')
        html_url = repo.get('html_url', '')
        updated_at = repo.get('updated_at', '')
        visibility = repo.get('visibility', '')
        writer.writerow([name, html_url, updated_at, visibility])


