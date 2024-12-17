from bs4 import BeautifulSoup
import requests
import csv

url = 'https://stackoverflow.com/questions/tagged/python'
page = requests.get(url)
# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
questions = soup.find_all('h3',attrs = {"class":"s-post-summary--content-title"})
for question in questions:
    print(question.get_text())
