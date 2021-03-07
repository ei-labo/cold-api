import requests
import os

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
    with open(os.path.join(PUBLIC_DIR, file['name']), 'wb') as f:
        content = requests.get(file['url'], stream=True).content
        f.write(content)
