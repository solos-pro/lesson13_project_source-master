import json

with open("posts.json", encoding='utf-8') as f:
    candidates = json.load(f)
for candidate in candidates:
    print(candidate,'/n')

def get_posts_by_tag():
    with open("posts.json", encoding='utf-8') as f:
        data = json.load(f)
    result = []
    tag = 'пирог'
    for record in data:
        if tag in record['content']:
            result.append(record)
    return result