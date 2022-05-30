from lib2to3.pgen2 import driver
from pylenium.driver import Pylenium

url = 'https://vk.com'
passwd = 'Pressxtogtfo1'
number = '+79809111725'



def test_vk(py: Pylenium):
    py.visit(url)
    py.webdriver.find_element_by_xpath('//*[@id="index_login"]/div/form/button[1]/span/span').click()
    py.get('[name="login"]').type(number).submit()
    py.get('[name="password"]').type(passwd).submit()
    assert py.should().contain_title('Новости')

