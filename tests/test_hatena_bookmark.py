import json

from playwright.sync_api import Page


def test_hatena_bookmark_hotentry(page: Page):
    url = "https://b.hatena.ne.jp/hotentry/all"
    page.goto(url)

    # 人気エントリーの一覧を取得
    entries = []
    entry_cards = page.locator("div.entrylist-contents").all()

    for card in entry_cards:
        # タイトルとURLの取得
        title_link = card.locator("h3.entrylist-contents-title a")
        title = title_link.text_content().strip()
        link_url = title_link.get_attribute("href")

        # ブックマーク数の取得
        bookmark_count_text = card.locator("span.entrylist-contents-users span").text_content().strip()
        # 数字のみを抽出（"123 users"のようなテキストから"123"を取得）
        bookmark_count = int(bookmark_count_text.split()[0])

        entries.append({"title": title, "url": link_url, "bookmark_count": bookmark_count})

    # JSON形式で出力
    print(
        json.dumps(
            entries,
            indent=2,
            ensure_ascii=False,
        )
    )
