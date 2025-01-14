from playwright.sync_api import Page


def test_nenkin(page: Page):
    url = "https://www2.nenkin.go.jp/do/search_section/"
    page.goto(url)

    corporate_number = "2010401092245"

    page.get_by_label("法人番号で検索する").check()
    page.get_by_label("法人番号（半角数字13桁）").fill(corporate_number)
    page.get_by_role("button", name="検索実行").click()
    num_of_employee = page.locator('//td[@class="search_right_top"]').inner_text()

    print(f"# of employee: {num_of_employee} people in {corporate_number}")
