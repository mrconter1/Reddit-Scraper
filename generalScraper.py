import time
import datetime
import os, errno
import urllib.request

#Retrieves html from url
def getHtml(url):
     
     req = urllib.request.Request(url)
     try: 
          html = urllib.request.urlopen(req).read().decode('utf8')
     except urllib.error.URLError as e:
          html = ""
          
     return html
     
#Retrives submissions/posts between certain dates by fetching links within a sliding time window
#Time window is due to reddit restriction
def getSubmissions(after, before, windowSize, subreddit):

     #Convert to unix time
     after = int(time.mktime(datetime.datetime.strptime(after, "%d/%m/%Y").timetuple()))
     before = int(time.mktime(datetime.datetime.strptime(before, "%d/%m/%Y").timetuple()))
     
     currentTime = after

     submissionLinks = []
     
     while currentTime < before:
     
          link = "https://api.pushshift.io/reddit/submission/search/?after=" + str(currentTime) + "&before=" + str(currentTime + windowSize) + "&sort_type=score&sort=desc&subreddit=" + subreddit
          html = getHtml(link)
          
          #Extract link to posts
          data = html.split('full_link": "')
          for post in data[1:]:
               postLink = post.split('",')[0]
               submissionLinks.append(postLink)
               
          currentTime += windowSize
          
          print("Number of posts collected: " + str(len(submissionLinks)))
          #Sleep to prevent to many requests
          time.sleep(60/200)
     
     return submissionLinks
     
#Saves result to file
def saveResults(submissionLinks):
     
     with open('posts.csv', 'a') as f:
          for post in submissionLinks:
               f.write(post) 
               f.write("\n")
          
#Run program
saveResults(getSubmissions("1/8/2016", "26/8/2018", 30*60, "dataisbeautiful"))










