from pylenium.driver import Pylenium

url = 'https://www.sberbank.ru/ru/person'

def test_sber(py: Pylenium):
    py.visit(url)
    py.webdriver.find_element_by_xpath('//*[@id="main-page"]/div[2]/div/div[4]/nav/div/ul/li[3]/a[1]').click()
    py.webdriver.find_element_by_link_text('Оформить ипотеку онлайн').click()
    assert py.contains('Ипотечный')
    