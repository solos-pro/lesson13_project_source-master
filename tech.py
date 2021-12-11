import json

with open("posts.json", encoding='utf-8') as f:
    candidates = json.load(f)
for candidate in candidates:
    print(candidate,'/n')
