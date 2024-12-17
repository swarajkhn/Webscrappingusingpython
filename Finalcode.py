#Importing modules to perform tasks
from bs4 import BeautifulSoup       #Used to parse HTML content
import requests                     #Used to send HTTP requests
import csv                          #Used to handle CSV file operations
import time                         #Used to introduce delay in script
import pandas as pd                 #Used to handle and manipulate data in table


#Function to scrape questions from a single page
def get_questions(url):
    #Send a GET request to the provided URL and store the response
    page = requests.get(url)
    # print(page.content)   #Uncomment to get the raw HTML content of the page
    soup = BeautifulSoup(page.content, "html.parser")   #Parse the HTML content using BeutifulSoup
    # Create a list to store the list of questions 
    loq = []
    #Find all question titles on the page
    questions = soup.find_all('h3',attrs = {"class":"s-post-summary--content-title"})
    #If no questions are found, return FALSE (used later to stop the loop)
    if not questions:
        return False
    #Loop through each question found and extract its text
    for question in questions:
        loq.append(question.get_text().strip()) #strip the space between questions
    #return the list of questions
    return loq

#the below commented code is to find list of questions for a single page
# url = 'https://stackoverflow.com/questions/tagged/python'
# listoq = get_questions(url)
# print(listoq)

#Splitting the URL so as to get all the pages
urlp1 = 'https://stackoverflow.com/questions/tagged/python?tab=newest&page='
urlp2 = '&pagesize=50'
pgno = 0

listofq = []    #Initialize an empty list to store all questions

#loop to scrape from multiple pages
while(True):
    time.sleep(0.5) #Pause for 0.5 seconds between requests to avoid overloading the server
    pgno += 1   #Increment the page number
    url = urlp1 + str(pgno) + urlp2 #Construct the URL by concatenating the string
    print(url)  #print the urls to know if all the pages is being obtained
    #call the function to get questions from the current page
    getq = get_questions(url)
    #break the loop if no more question exists
    if getq == False:
        break
    #add the questions from the current page to the main list of all the questions
    listofq.extend(getq)

#Print the total number of questions scraped for verification
print(len(listofq))

#Create a dataframe and save to a CSV file
data = {'questions':listofq}    #Create a dictionary with the questions
df = pd.DataFrame(data)         #Convert the dictionary to a pandas dataframe

#Save the dataframe to a CSV file named 'DATA.csv' in the directory you are running the code
df.to_csv('./DATA.csv')

