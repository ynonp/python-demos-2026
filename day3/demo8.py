import threading
from concurrent.futures import ThreadPoolExecutor
import time
import httpx

book_urls = [
        "https://www.gutenberg.org/cache/epub/84/pg84.txt",
        "https://www.gutenberg.org/cache/epub/45304/pg45304.txt",
        "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
        ]

def download_url(url: str):
    r = httpx.get(url)
    size = len(r.text)
    return {"url": url, "size": size}


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as p:
        results = p.map(download_url, book_urls)

        for result in results:
            print(result)

