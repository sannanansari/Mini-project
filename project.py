# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:56:49 2019

@author: Ansari
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:09:14 2018
@author: Ansari
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:48:37 2019

@author: Ansari
"""


import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []
        self.p,self.neg,self.neu,self.search=0,0,0,0
        self.term = ''
    def DownloadData(self):
        consumerKey = ""
        consumerSecret = ""
        accessToken = ""
        accessTokenSecret = ""
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        searchTerm = v.get()
        NoOfTerms = 100

        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

        csvFile = open('result.csv', 'a')

        csvWriter = csv.writer(csvFile)


        polarity = 0
        positive = 0
        negative = 0
        neutral = 0
        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity

            if (analysis.sentiment.polarity == 0):
                neutral += 1
            elif (analysis.sentiment.polarity > 0.0 and analysis.sentiment.polarity <= 0.9):
                positive += 1
            elif (analysis.sentiment.polarity > -0.9 and analysis.sentiment.polarity <= -0.0):
                negative += 1
            
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        positive = self.percentage(positive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        polarity = polarity / NoOfTerms

        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0.0 and polarity <= 1.0):
            print("Positive")
        elif (polarity > -1.0 and polarity <= -0.0):
            print("Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(negative) + "% people thought it was negative")
        print(str(neutral) + "% people thought it was neutral")
        self.p = positive
        self.neg = negative
        self.neu = neutral
        self.term = NoOfTerms
        self.search = searchTerm
        return self.p,self.neg,self.neu,self.search,self.term
    def cleanTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')


import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter
from tkinter import *
gui = Tk()
gui.state('zoomed')
gui.configure(background='#38A1F3')

#Label-heading
l = Label(gui,text='Welcome to Twitter sentimental Analysis',fg='white',bg= '#38A1F3',height=10)
font = ('times',20,'bold')
l.config(font=font)
l.pack(anchor='center')

#Label-text
label = Label(gui,text='Enter the input Here',bg='#38A1F3',fg='white').pack()
label = Label(gui,text='Enter the input Here',fg='#38A1F3',bg='#38A1F3').pack()

#Input
v = StringVar()
entry = Entry(gui,bd=3,width=45,textvariable=v).pack()
label = Label(gui,text='Enter the input Here',fg='#38A1F3',bg='#38A1F3').pack()

#button
def newframe():
    frame = Toplevel(gui)
    label = Label(frame,text=v.get()).pack()
    sa = SentimentAnalysis()
    positive, negative, neutral, searchTerm, noOfSearchTerms=sa.DownloadData()
    def plotPieChart(positive, negative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]']
        sizes = [positive, neutral, negative]
        colors = ['yellowgreen', 'gold', 'red']
        #patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        #plt.legend(patches, labels, loc="best")
        fig = matplotlib.figure.Figure(figsize=(5,5))
        ax = fig.add_subplot(111)
        ax.pie(sizes) 
        ax.legend(colors)
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        ax.add_artist(circle)
        window= tk.Tk()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        window.mainloop()
        
    plotPieChart(positive, negative, neutral, searchTerm, noOfSearchTerms)
    button = Button(frame,text='click here to quit',command=frame.destroy).pack()
    
button = Button(gui,text='Calculate sentiment',command=newframe).pack()

gui.mainloop()
print(x)
