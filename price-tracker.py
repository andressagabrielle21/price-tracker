import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "" #Type, between the quotations, the URL you want to track

headers = {"User-Agent": "", "Pragma":"no-cache"} #Type "User-agent" in your browser, and copy onto the first quotation after "User-Agent:"

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    
    title = soup.find(id="").get_text() #Type, between the quotations, the id of the TITLE of your product
    price = soup.find(id="").get_text() #Type, between the quotations, the id of the PRICE of your product
    

    converted_price = float(price[2:5])

    if(converted_price < 1): #Instead of 1, type your desired price
        send_mail()

    print(title.strip())
    print("VALUE = ", converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #Comand sent by an email server to identify itself when connecting to another email server
    server.starttls()
    server.ehlo()

    server.login("", "") 
    #Inside the first quotation, type your email
    #And inside the second one, type the password that you generate in "Google Two-Step Validation"

    subject = "HEY! The price has decreased!"
    body = "CHECK IT OUT: " #Type your prefered message for when 

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "", #Type, between the quotations, your email
        "", #Type, between the quotations, your email
        msg
    )

    print("SENT")
    server.quit()

while(True):
    check_price()
    time.sleep(86400) #This time.sleep will check if the price of your desired product reached the your desired price ONCE A DAY. You can change it easily, always making sure you put into seconds.