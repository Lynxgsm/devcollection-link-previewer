from linkpreview import link_preview
import pdfkit
import sys
import json
from time import sleep

Instance = None


def main():
    try:
        pdfkit.from_url(
            'https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField', 'shaurya.pdf')
        preview_link(
            "https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField")
        print({"message": "Starting browser"})

    except Exception as e:
        print({"message": f"Something went wrong with the browser. {e}"})
        sleep(1)


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
