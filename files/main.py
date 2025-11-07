import scrape
import requests
import random
import sys

if len(sys.argv) < 4:
    print("Usage: python3 main.py <formUrl> <numResponses> <typedResponseOutcomesList>")
    sys.exit(1)

url = sys.argv[1].replace('viewform', 'formResponse')        
numResponses = int(sys.argv[2]) 
typedResponseOutcomes = sys.argv[3].split(",") if sys.argv[3] else []

fields = scrape.scrapeFields(url)
payload = {}

for _ in range(numResponses):
    for fid, data in fields.items():
        if data['options']:
            if data['type'] == 'checkbox':
                noSelections = random.randint(1, len(data['options']))
                selections = set()

                for i in range(noSelections):
                    selections.add(random.choice(data['options']))
                payload[fid] = selections
                continue

            payload[fid] = random.choice(data['options'])

        else:
            if len(typedResponseOutcomes) > 1:
                noOutcomes = random.randint(1, len(typedResponseOutcomes))
                outcomes = set()

                for i in range(noOutcomes):
                    outcomes.add(random.choice(typedResponseOutcomes))
                payload[fid] = outcomes
                continue

            payload[fid] = "" if not data['required'] else typedResponseOutcomes[0]

    requests.post(url, data=payload)
