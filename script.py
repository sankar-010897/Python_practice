import requests
import smtplib

# API Key
api_file = open('apikey.txt', 'r')
api_key = api_file.read()
api_file.close()

#Home address
home = input("Enter your Home Address\n")

#Work address
work = input("Enter your Work Address\n")

#base URL
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

#get requests
r = requests.get(url + "origins=" + home + "&destination=" + work + "&key=" + api_key)
print(r)
#get output as time in seconds and texts
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][1]["duration"]["value"]

print("\n The total travel time from home to work is",time )

#check if travel time is more than 2 Hrs
if seconds > 7200:
    #email constraints
    sender = "sankara.muthy@gmail.com"
    recipient = "sankara.muthy@outlook.com"
    subject = "Sick Day"

    #format email
    email = "Subject: {}\n\n Sorry, but I can't make it work today."

    #get sender mail
    pwd_file = open('pwd.txt', 'r')
    password = pwd_file.read()
    pwd_file.close()

    #create SMTP session
    s = smtplib.SMTP("smptp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # authentication
    s.login(sender, password)
    #send the mail
    s.sendmail(sender, recipient, email)
    #terminating the session
    s.quit()
    #print message
    print("\n The email was sent sucessfully to ", recipient," since the travel time was too long")