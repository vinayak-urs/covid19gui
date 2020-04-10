import tkinter as tk
from tkinter import font, Canvas, Frame, Button
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import time
import threading


def getdata(url):
    r = requests.get(url)
    return r.text


def firstelemnt(lst):
    return lst[0]


def update():
    # this portion is the soup from the mohfw.gov.in
    myHtmldata = getdata("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmldata, "html.parser")

    rawStatus = ""

    # here the parsed html will be shaped in the desired data string
    for tr in soup.find_all("tbody")[0].find_all("tr"):
        rawStatus += tr.get_text()
    rawStatus = rawStatus[1:]
    # This is the statewise divided data of the whole data
    pureStatus = rawStatus.split("\n\n")

    # this is data of the all states/city in list format
    stateData = pureStatus[:31]

    # This is the data of the india collectively
    restData = pureStatus[31:32]
    restData2 = []
    restData2 = pureStatus[32:34]

    # string to manipulate the data of the india from the website in the respective manner
    india_str = ""
    for i in restData:
        india_str += i

    india_str += "\n"

    for i in restData2:
        india_str += i

    # Whole string of the india is piled now time to mantain in a single string
    indiaData = []
    indiaData = india_str.split("\n")

    # Updating the sreial no of the india
    indiaData.insert(0, 32)
    indiaData[1] = "INDIA"

    # Cloning the data to the new list
    orData = []
    for item in stateData:
        orData.append(item.split("\n"))

    # maitining the string data in the int data as far as ease of the sorting and all things

    for item in orData:
        item[0] = int(item[0])
        item[2] = int(item[2])
        item[3] = int(item[3])
        item[4] = int(item[4])
    orData.sort(key=firstelemnt, reverse=False)

    orData.append(indiaData)
    # print("STATES/CITY  CASES CURED DIED")
    r = 6
    for d in orData:
        c = 0
        for p in d:
            tk.Label(text=p, width=27, relief=tk.RIDGE).grid(row=r, column=c)
            c = c+1
        r = r+1
    # print(ordata)
    time.sleep(10)


# Basics configurations
root = tk.Tk()
root.geometry("1000x800")
root.configure(bg="gray")
image = Image.open("2.png")
tk_image = ImageTk.PhotoImage(image)

#  main hording of the COVID19
label = tk.Label(root, text="COVID19-INDIA",
                 font="Anton 30 bold", image=tk_image, compound="center")
label.grid(row=0, column=0, columnspan=5)


# main label for the data representation
tk.Label(text="SR.NO.", relief=tk.RIDGE, width=27).grid(
    row=5, column=0)
tk.Label(text="STATES/CITY", relief=tk.RIDGE, width=27).grid(row=5, column=1)
tk.Label(text="ACTIVE CASES", relief=tk.RIDGE, width=27).grid(row=5, column=2)
tk.Label(text="RECOVERED", relief=tk.RIDGE, width=27).grid(row=5, column=3)
tk.Label(text="DEATH", relief=tk.RIDGE, width=27).grid(
    row=5, column=4)

# data feed for the rest of the column
root.after(5000, update)


# last two buttons for the refresh and exit the program
frame = Frame(root, borderwidth=10, bg="grey",
              relief=tk.SUNKEN).grid(row=40, column=0, ipadx=50)
frame2 = Frame(root, borderwidth=10, bg="grey",
               relief=tk.SUNKEN).grid(row=40, column=4, ipadx=50)
b1 = Button(frame, fg="red", text="REFRESH", command=threading.Thread(
    target=update)).grid(row=40, column=0, ipadx=50)
b2 = Button(frame2, fg="red", text="EXIT", command=exit).grid(
    row=40, column=4, ipadx=50)
time.sleep(20)
root.mainloop()
