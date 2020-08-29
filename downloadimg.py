from itertools import islice
from fbchat import Client
from fbchat.models import *
import urllib.request
import getpass
import os
import getpass
from datetime import datetime

uid = input("Username: ")
pas = getpass.getpass("Password: ")

client = Client(uid, pas)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_time = str(current_time)
username = getpass.getuser()
par = "/home/" + username + "/Downloads/"
path = os.path.join(par, "messanger/")
try:
    os.mkdir(path)
except OSError as error:  
    print(error) 
path = os.path.join(path, current_time)
os.mkdir(path)

i = 0
grpid = input("User / Group ID: ")
# grpid = "100006503047216"
cnty = int(input("How much: "))

images = client.fetchThreadImages(grpid)

for image in islice(images, cnty):
    i = i + 1
    # print(image.large_preview_url)
    try:
        urllib.request.urlretrieve(image.large_preview_url, str(path)+ "/" + str(i)+".jpg")
    except Exception as er:
        print(er)
