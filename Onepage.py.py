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

# with open('questions.csv', 'w', newline = '') as file:
#     for question in questions:
#         writer = csv.writer(file)
#         writer.writerow(question)
#     print("Data has been written to 'questions.csv'")


# url = 'https://stackoverflow.com/questions/tagged/python'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html")
# print(soup.prettify())
# questions = soup.find_all('div', class_= 's-link')
# for question in questions:
#     print(question)

# with open('questions.csv', 'w', newline = '') as file:
#     for question in questions:
#         writer = csv.writer(file)
#         writer.writerow(question)
#     print("Data has been written to 'questions.csv'")