from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from linkpreview import link_preview

import sys
import json
from time import sleep

# SET OPTIONS
chrome_options = Options()
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--headless")

Instance = None


def main():

    global Instance

    try:
        create_directory()
        Instance = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)

        preview_link(
            "https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField")

        # Instance.execute_script('window.print();')

        print({"message": "Starting browser"})

    except Exception as e:
        print({"message": f"Something went wrong with the browser. {e}"})
        sleep(1)
        Instance.quit()


def preview_link(link):
    try:
        preview = link_preview(link)
        print("title:", preview.title)
        print("description:", preview.description)
        print("image:", preview.image)
        print("force_title:", preview.force_title)
        print("absolute_image:", preview.absolute_image)
    except Exception as e:
        print({"message": f"Something went wrong with the link preview. {e}"})


if __name__ == "__main__":
    main()
