from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from collections import defaultdict
import os
import requests
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def click_element_by_xpath(xpath):
    try:
        element = driver.find_element(by=By.XPATH, value=xpath)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except Exception as e:
        # print(f"Error clicking element {xpath}: {e}")
        pass

def get_element_text_by_xpath(xpath):
    try:
        element = driver.find_element(by=By.XPATH, value=xpath)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element.text
    except Exception as e:
        # print(f"Error getting text from element {xpath}: {e}")
        return "None"
    
try:
    driver.get("https://elpais.com/")
    print("Successfully opened the website.")

    # Close the dialogue box (Cookies Policy)
    # Click on the "Accept/Aceptar" button
    # time.sleep(5)
    try:
        element = driver.find_element(by=By.XPATH, value='//*[@id="didomi-notice-agree-button"]')
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
        element.click()
    except Exception as e:
        # print(f"Error clicking element {xpath}: {e}")
        pass
    
    click_element_by_xpath('//*[@id="pmConsentWall"]/div/div/div[2]/div[1]/a')

    #  Ensuring the page is in Spanish
    #time.sleep(5)
    if get_element_text_by_xpath('//*[@id="edition_head"]/a/span') == "ESPAÑA":
        print("The page is in Spanish")
    else:
        print("The page is not in Spanish")

    # Scrape top 5 articles fromt the Opinion section
    # time.sleep(5)
    click_element_by_xpath('//*[@id="csw"]/div[1]/nav/div/a[3]')

    # Initialize variables
    article_links = []
    max_articles = 5  # Number of articles to fetch
        # Locate all <article> elements on the page
    articles = driver.find_elements(By.TAG_NAME, "article")

    # Loop through each article and extract desired information
    for index, article in enumerate(articles, start=1):
        # Fetch article header if present
        try:
            header = article.find_element(By.TAG_NAME, "header").text
        except:
            header = "No header found"

        # Fetch article link if present
        try:
            link_element = article.find_element(By.TAG_NAME, "a")
            link = link_element.get_attribute("href")
            article_links.append(link)
        except:
            link = "No link found"

    #Open each articles one by one and store the title, content and the image in a "article_images" folder in the current directory and save the image with the title of the article

    # Initialize variables
    articles = defaultdict(dict)

    # Create the directory for saving images if it doesn't exist
    if not os.path.exists("article_images"):
        os.makedirs("article_images")

    itr=1
    # Iterate through the collected links
    for idx, link in enumerate(article_links, start=1):
        # Open the link in a new tab
        driver.execute_script("window.open(arguments[0], '_blank');", link)
        driver.switch_to.window(driver.window_handles[-1])
        driver.set_page_load_timeout(10)
        #time.sleep(5)
        
        try:
            # Extract article title
            title = get_element_text_by_xpath("/html/body/article/header/div[1]/h1")
            if title is "None":
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                continue
            
            # Extract article content
            content = get_element_text_by_xpath("/html/body/article/header/div[1]/h2")
            if content is "None":
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                continue
            
            # Extract article image within the article element
            article_element = driver.find_element(By.TAG_NAME, "article")
            images = article_element.find_elements(By.TAG_NAME, "img")
            if not images:
                images = ["No image found"]
            else:
                images = [image.get_attribute("src") for image in images]

                # Store the article data
                articles[idx] = {
                    "title": title,
                    "content": content,
                    "image": images[0],
                }
                
                # Save the image
                driver.get(images[0])
                driver.save_screenshot(os.getcwd() + f"/article_images/{title}.png")
                
                print(f"Article {itr}\n Title: {title}\n Content: {content}\n Image link: {images[0]}\n")
        
        except Exception as e:
            print(f"Error accessing {link}: {e}")

        # Close the tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        if itr == max_articles:
            break
        itr+=1

    driver.quit()

    # Translate the titles of the articles to English using the Google Translate API
    def translate_text(text, from_lang="es", to_lang="en"):
        try:
            url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"
            payload = {
                "from": from_lang,
                "to": to_lang,
                "html": text
            }
            headers = {
                "x-rapidapi-key": "989ba4021amsh77404cec44a4edap1b7005jsnc38adc501a21",
                "x-rapidapi-host": "google-translate113.p.rapidapi.com",
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return response.json().get("trans", text)
            else:
                print(f"Translation failed for '{text}': {response.text}")
                return text
        except Exception as e:
            print(f"Error translating '{text}': {e}")
            return text

    # Translate the titles of the articles to English
    itr = 1
    for idx, article in articles.items():
        title = article["title"]
        translated_title = translate_text(title)
        articles[idx]["translated_title"] = translated_title

        print(f"Article {itr}\n Title: {title}\n Translated Title: {translated_title}\n")
        itr+=1


    # Count the number of occurance of the repeated words in the translated titles of the articles
    # Print the count of each word along wiht the word
    def count_words(text):
        words = text.lower().split()
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        return word_count

    # Aggregate word counts across all translated titles
    word_counts = defaultdict(int)
    for idx, article in articles.items():
        translated_title = article["translated_title"]
        word_count = count_words(translated_title)
        for word, count in word_count.items():
            word_counts[word] += count

    # Identify and print words repeated more than twice
    print("Words repeated more than twice across all headers:")
    has_words_repeated = False
    for word, count in word_counts.items():
        if count > 2:
            print(f"{word}: {count}")
            has_words_repeated = True

    if not has_words_repeated:
        print("No words repeated more than twice found in the translated titles.")

    # Set the status of the test as 'passed'
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All steps executed successfully!"}}')
except NoSuchElementException as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
finally:
    # Stop the driver
    driver.quit()
