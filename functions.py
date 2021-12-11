import json

def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def get_tags(data):
    result = set()

    for record in data:
        content = record['content']
        words = content.split()

        for word in words:
            if word.startswith('#'):
                print(word[:])
                result.add(word[1:])
    return result

