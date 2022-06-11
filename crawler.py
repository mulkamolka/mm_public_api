from typing import Dict
from util.calc import calc_time
import requests

@calc_time
def api_call(api_url: str) -> Dict:
    try:
        res = requests.get(api_url, timeout=5.0)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return res.json()