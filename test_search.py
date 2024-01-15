from selene import browser, be, have


def test_search_first():
    browser.open('https://google.com')
    browser.element('[name="q"]') \
        .should(be.blank) \
        .type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_second():
    browser.open('https://google.com')
    browser.element('[name="q"]') \
        .should(be.blank) \
        .type('3g4gmp 4gm4').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу 3g4gmp 4gm4 ничего не найдено. '))
