from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

        Instance.get(
            "https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField")

        Instance.execute_script('window.print();')

        print({"message": "Starting browser"})

    except Exception as e:
        print({"message": f"Something went wrong with the browser. {e}"})
        sleep(1)
        Instance.quit()


if __name__ == "__main__":
    main()
