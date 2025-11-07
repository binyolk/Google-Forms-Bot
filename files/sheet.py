import requests, pandas, random

PATH = "data.csv"

def updateCSV(sheetID, sheetName):
    sheetURL = f"https://docs.google.com/spreadsheets/d/{sheetID}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    response = requests.get(sheetURL)

    with open('data.csv', 'wb') as f:
        f.write(response.content)


def buildWeightedDistributions(csvPath):
    df = pandas.read_csv(csvPath)
    weights = {}
    for col in df.columns[1:]: 
        series = df[col].dropna().astype(str)
        expanded = []
        for entry in series:
            if ',' in entry:
                expanded.extend([v.strip() for v in entry.split(',')])
            else:
                expanded.append(entry.strip())
        freq = pandas.Series(expanded).value_counts(normalize=True).to_dict()
        weights[col] = freq
    return weights


def sampleAnswer(question, weights):
    if question not in weights:
        return None
    options, probs = zip(*weights[question].items())
    return random.choices(options, probs)[0]


def sampleMultiAnswer(question, weights):
    if question not in weights:
        return []
    options, probs = zip(*weights[question].items())
    n = random.randint(1, len(options))
    return random.choices(options, probs, k=n)

