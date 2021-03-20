import requests
import os
import json

PUBLIC_DIR = "public"
FILES = [{
    "url": "https://storage.googleapis.com/cold-api/artifacts_config.json",
    "name": "artifacts_config.json",
}, {
    "url": "https://storage.googleapis.com/cold-api/contracts.json",
    "name": "contracts.json",
}, {
    "url": "https://storage.googleapis.com/cold-api/live_config.json",
    "name": "live_config.json",
}, {
    "url": "https://storage.googleapis.com/cold-api/mission_reward_count.json",
    "name": "mission_reward_count.json",
}]

for file in FILES:
    content = requests.get(file['url'], stream=True).content
    with open(os.path.join(PUBLIC_DIR, file['name']), 'wb') as f:
        f.write(content)
    if file['name'].endswith('.json'):
        with open(os.path.join(PUBLIC_DIR, file['name'][:-5] + '.pretty.json'), 'w') as f:
            data = json.loads(content)
            json.dump(data, f, indent=2, ensure_ascii=False)
