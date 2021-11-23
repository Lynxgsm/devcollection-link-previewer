from linkpreview import link_preview
import pdfkit
import sys


def preview_link(link: str):
    try:
        preview = link_preview(link)
        print({
            'title': preview.title,
            'description': preview.description
        })
    except Exception as e:
        print({"message": f"Something went wrong with the link preview. {e}"})


def download(url):
    try:
        pdfkit.from_url(
            'https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField', './articles/.pdf')
        preview_link(
            "https://stacksecrets.com/flutter/flutter-textfield-decoration-in-depth#Customizing_The_Look_And_Feel_Of_TextField")

    except Exception as e:
        print({"message": f"Something went wrong with the browser. {e}"})
        sleep(1)


# if sys.argv[1] == "preview":
#     preview_link(sys.argv[2])
# elif sys.argv[1] == "download":
#     download()

preview_link(sys.argv[1])
