import scrape, requests, sys, sheet

if len(sys.argv) < 5:
    print("Usage: python3 main.py <formUrl> <numResponses> <sheetID> <sheetName>")
    print("Example: python3 main.py https://docs.google.com/forms/d/e/.../viewform 10 '1abcD2EfGhIJ3klMN4opQR5stUV' 'Form responses 1'")
    sys.exit(1)

url = sys.argv[1].replace('viewform', 'formResponse')        
numResponses = int(sys.argv[2])
sheetID = sys.argv[3]
sheetName = sys.argv[4] if sys.argv[4] else "Form responses 1"

sheet.updateCSV(sheetID, sheetName)

fields = scrape.scrapeFields(url)
weights = sheet.buildWeightedDistributions("data.csv")

for _ in range(numResponses):
    payload = {}
    for fid, data in fields.items():
        q = data['question']
        if data['type'] == 'checkbox':
            payload[fid] = sheet.sampleMultiAnswer(q, weights)
        elif data['options']:
            payload[fid] = sheet.sampleAnswer(q, weights)
        else:
            payload[fid] = sheet.sampleAnswer(q, weights) or ""
    requests.post(url, data=payload)