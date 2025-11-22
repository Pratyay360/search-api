import asyncio
import time
from random import shuffle
from typing import List, Optional

import urllib3
from ddgs import DDGS
urllib3.disable_warnings()


async def search(query: str, max_results: int = 10):
    max_retries = 7
    ddgs = DDGS(timeout=100)
    for attempt in range(max_retries):
        try:
            results = ddgs.text(query, max_results=max_results)
            res = [] 
            for  result in results:
                res.append(result.get('href', 'No URL'))
            return res
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
                continue
            else:
                raise RuntimeError(f"Search failed after {max_retries} attempts")

if __name__ == "__main__":
    query = "Python programming"
    max_results = 15
    start_time = time.time()
    results = asyncio.run(search(query, max_results))
    end_time = time.time()
    print(f"Search completed in {end_time - start_time:.2f} seconds")
    print(f"Results: {results}")
