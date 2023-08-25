from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def youtube(driver,sorgu):
    driver.get("https://www.youtube.com")
    time.sleep(1)
    search_box = driver.find_element("name", "search_query")
    time.sleep(1)
    search_box.send_keys(sorgu)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

def google(driver,sorgu):
    driver.get("https://www.google.com")
    time.sleep(1)
    search_box = driver.find_element("name", "q")
    time.sleep(1)
    search_box.send_keys(sorgu)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    input("Sayfanın ilk kelimesini gir:")

    # Get the list of search results
    results = driver.find_elements_by_css_selector("div.rc")

    # Print the titles of the search results
    for i, result in enumerate(results):
        title = result.find_element_by_css_selector("h3").text
        print(f"{i + 1}. {title}")

    # Ask the user to select a result
    index = int(input("Enter the index of the result you want to visit: ")) - 1

    # Click on the selected result
    result_link = results[index].find_element_by_css_selector("a")
    result_link.click()

    time.sleep(1)

    input("Kapatmak için Enter...")
    driver.quit()

adres = input("Nerede aransın:")
aranacak = input("Ne aransın?:")

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(options=chrome_options)

if adres == youtube:
    youtube(driver,aranacak)
else:
    google(driver,aranacak)

