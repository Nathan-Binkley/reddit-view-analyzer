import csv
import json
import pandas as pd

with open('out.json', 'r') as f:
    data = json.load(f)

def views_to_readable(views):
    if views == "N/A":
        return "N/A"
    if views[-1] == "k":
        return int(float(views[:-1]) * 1000)
    return int(views)

with open('out.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['url', 'views', 'upvote_ratio', 'shares', 'current_score'])
    for i in data:
        writer.writerow([i['url'], views_to_readable(i['views']), i['upvote_ratio'], i['shares'], i['current_score']])

read_file = pd.read_csv (r'out.csv')
read_file.to_excel (r'out.xlsx', index = None, header=True)