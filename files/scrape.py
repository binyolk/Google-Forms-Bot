import re, requests, demjson3

def scrapeFields(formUrl):
    res = requests.get(formUrl)
    match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (.*?);</script>', res.text, re.S)
    if not match:
        print('No embedded form data found.')
        return {}

    dataStr = match.group(1)
    rawData = demjson3.decode(dataStr)
    formData = rawData[1][1]

    fields = {}

    for item in formData:
        if not item or len(item) < 5 or not item[4]:
            continue

        try:
            qid = item[4][0][0]
            qtext = item[1]
            qtype = item[3]

            required = False
            if len(item[4][0]) > 2:
                required = item[4][0][2] == 1

            if qtype == 2:
                opts = item[4][0][1]
                options = [opt[0] for opt in opts if opt and opt[0].strip()]
                fields[f'entry.{qid}'] = {
                    'question': qtext,
                    'type': 'choice',
                    'options': options,
                    'required': required
                }
            elif qtype == 4:
                opts = item[4][0][1]
                options = [opt[0] for opt in opts if opt and opt[0].strip()]
                fields[f'entry.{qid}'] = {
                    'question': qtext,
                    'type': 'checkbox',
                    'options': options,
                    'required': required
                }
            elif qtype == 5:
                opts_raw = item[4][0][1]
                options = [o[0] for o in opts_raw if o and o[0].strip()]
                fields[f'entry.{qid}'] = {
                    'question': qtext,
                    'type': 'linear',
                    'options': options,
                    'required': required
                }
            elif qtype in (0, 1):
                fields[f'entry.{qid}'] = {
                    'question': qtext,
                    'type': 'text',
                    'options': None,
                    'required': required
                }

        except Exception:
            continue

    return fields
