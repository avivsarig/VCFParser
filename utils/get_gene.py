import json
import requests
import time
import os

API_URI = os.getenv("API_URI", "https://test.genoox.com/api/fetch_variant_details")
CACHE_FILE = "gene_cache.json"

with open(CACHE_FILE) as f:
    cache = json.load(f)

MAX_RETRIES = 5
RETRY_DELAY = 3


def get_gene_payload(line):
    payload = {
        "chr": line["CHROM"],
        "pos": line["POS"],
        "ref": line["REF"],
        "alt": line["ALT"],
        "reference_version": "hg19",
    }
    return payload


def get_gene_from_cache(key):
    return cache.get(key)


def update_cache(key, value):
    cache[key] = value
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def fetch_gene_from_api(payload):
    for attempt in range(MAX_RETRIES):
        try:
            res = requests.post(API_URI, json=payload)
            res.raise_for_status()
            gene = res.json()["gene"]
            return gene

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Attempt {attempt + 1} of {MAX_RETRIES}")
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error with fetching gene from API for:\n{payload}")
            print(f"Exception: {e}")
            return False

    return None


def gene_from_api(line):
    payload = get_gene_payload(line)
    key = str(payload)

    gene = get_gene_from_cache(key)
    if gene:
        return gene

    gene = fetch_gene_from_api(payload)
    if gene:
        update_cache(key, gene)

    return gene
