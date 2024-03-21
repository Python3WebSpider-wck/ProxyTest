from selenium import webdriver

proxy = '127.0.0.1:7890'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get('https://httpbin.org/get')
print(browser.page_source)
browser.close()
