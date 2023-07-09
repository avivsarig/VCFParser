import json
import requests
import time
from utils.config import API_URI

with open("gene_cache.json") as f:
    cache = json.load(f)

MAX_RETRIES = 5
RETRY_DELAY = 3

def gene_from_api(line):
    payload = {
        "chr": line["CHROM"],
        "pos": line["POS"],
        "ref": line["REF"],
        "alt": line["ALT"],
        "reference_version": "hg19",
    }

    key = str(payload)
    if key in cache:
        return cache[key]
    else:
        for attempt in range(MAX_RETRIES):
            try:
                res = requests.post(API_URI, json=payload)
                res.raise_for_status()
                cache[key] = res.json()["gene"]

                with open("gene_cache.json", "w") as f:
                    json.dump(cache, f)

                return res.json()["gene"]

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}. Attempt {attempt + 1} of {MAX_RETRIES}")
                time.sleep(RETRY_DELAY)
            
            except Exception as e:
                print(f"Error with fetching gene from API for:\n{payload}")
                print(f"Exception: {e}")
                return False
