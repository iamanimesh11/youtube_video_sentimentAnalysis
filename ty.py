import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options = Options()



from bs4 import BeautifulSoup

def scrape_comments(url):
    # edge_driver_path = EdgeChromiumDriverManager().install()
    # options = webdriver.EdgeOptions()
    # options.headless = True
    # options.add_argument("--mute-audio")
    # service = Service(executable_path= edge_driver_path)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    time.sleep(5)

    # Scroll down the page to load more comments dynamically
    prev_height = 0
    while True:
        # Scroll down by 1000 pixels each time (adjust this value as needed)
        driver.execute_script(f"window.scrollTo(0, {prev_height + 2150});")
        time.sleep(1)
        prev_height += 2150

        # Get the current page height
        current_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        # If the previous height and the current height are the same, it means we've reached the bottom of the page
        if prev_height >= current_height:
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    title_text_div = soup.select_one('#container h1')
    title = title_text_div and title_text_div.text
    comment_div = soup.select("#content #content-text")
    comment_list = [x.text for x in comment_div]
    return comment_list, len(comment_list)
    # Your code for scraping comments using BeautifulSoup goes here


if __name__ == "__main__":
    st.title("YouTube Comments Scraper")

    # Get input URL from the user
    url = st.text_input("Enter YouTube video URL:")

    if st.button("Scrape Comments"):
        if url.startswith("https://www.youtube.com/watch?v="):
            comments, total_comments = scrape_comments(url)
            st.header("Scraped Comments")
            for comment in comments:
                st.write(comment)

            st.write(f"Total Comments: {total_comments}")
        else:
            st.warning("Invalid YouTube URL. Please enter a valid YouTube video URL.")
