import requests


def trans(code, url, apikey):
    r = requests.post(url, params={"key": apikey}, data={"q": code})
    if r.ok:
        return r.content
    return ""
