import json
from urllib.parse import urljoin

from playwright.sync_api import Page


def test_yahoo_realtime(page: Page):
    url = "https://search.yahoo.co.jp/realtime"
    page.goto(url)

    keywords = []

    for i in range(1, 21):
        locator = page.get_by_role(role="link", name=str(i), exact=True)
        keywords.append(
            {
                "text": locator.text_content(),
                "url": urljoin(url, locator.get_attribute("href")),
            }
        )
    # json output
    print(
        json.dumps(
            keywords,
            indent=2,
            ensure_ascii=False,
        )
    )
