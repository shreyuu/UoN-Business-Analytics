from bs4 import BeautifulSoup
import string

def remove_html(reviews):
    return [
        BeautifulSoup(d, "html.parser").get_text() 
        for d in reviews
    ]

