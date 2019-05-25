#!/home/dd/anaconda3/bin/python

import re, requests, sys, time
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
from selenium.webdriver import Firefox
assert opts.headless  # operating in headless mode

def main(url):
    """Takes dr.dk program URL, returns program .m3u8 URL."""

    # url example 'https://www.dr.dk/tv/se/hammerslag-tv/-/hammerslag-sma-huse-til-store-penge'

    browser = Firefox(options=opts)
    browser.get(url)
    time.sleep(5)   # change to 5 or higher to adjust for slow internet connection speed

    html = browser.execute_script("return document.getElementsByTagName('video')[0].innerHTML")
    m = re.search('\"(.+?\.m3u8)\"', html)
    result = m.group(1)
    browser.close()

    return result


if __name__ == '__main__':
    print(main(sys.argv[1]))