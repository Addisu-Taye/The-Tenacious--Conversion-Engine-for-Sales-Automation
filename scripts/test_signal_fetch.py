import json
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
    url = "https://www.ycombinator.com/jobs"

    Path("configs").mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        data = {
            "url": url,
            "title": page.title(),
            "content_preview": (page.text_content("body") or "")[:500],
        }

        with open("configs/job_signal_sample.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        browser.close()

    print("Saved configs/job_signal_sample.json")

if __name__ == "__main__":
    main()