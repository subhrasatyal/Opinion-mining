import sys,time,urllib2
from bs4 import BeautifulSoup

#Capturing the start time of this program
start_time = time.clock()

#Website used for parsing
website = str('zomato.com')

#Initializing browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

#create a new file and open a connection to it.
fileWriter=open('reviews.txt','w')
fileReader=open('in2.txt')

#Initializing index
index=0

#Creating the list to store all the records 
ReviewList = []
RatingList=[]
DateList=[]

for line in fileReader:
    #Fetch the url from file in2.txt    
    reviewlink = line.strip()   
    print reviewlink

    if reviewlink:
        page=0    
        while True:
            url = reviewlink + str(page)
            #Opening the url    
            try:
                response=browser.open(url,timeout=(5.0))
                time.sleep(2) 
            except Exception as e:
                error_type, error_obj, error_info = sys.exc_info()
                print 'ERROR FOR URL:',url
                print error_type, 'Line:', error_info.tb_lineno
                continue
            
            #Initializing Beautifulsoup object
            html = response.read()
            bsObj = BeautifulSoup(html)
            
            for date in bsObj.findAll('div', attrs={'class':'card search-snippet-card  search-card '}):
                DateList.append(date.text.strip())

            #Will parse the Reviews and append it to the list
            for review in bsObj.findAll("div aria label",{"class": "ttupper fs12px left bold zdhl2 tooltip icon-font-level-7" 
                ReviewList.append(review.text.replace('\n', ' ').strip('\n')) 
    
            #Will parse the Ratings and append it to the list
            for rating in bsObj.findAll("div", attrs={'class':'rating-popup'}):
                RatingList.append(rating['title'].strip()) 
   
            
            #Comparing length and writing data to file.            
            if len(DateList) == len(ReviewList) == len(RatingList):
                index = 0
                while (index < len(ReviewList)):
                    fileWriter.write(website + '\t' + ReviewList[index].encode('utf8') +'\t'+ RatingList[index].encode('utf8') + '\t' + DateList[index].encode('utf8')+'\n')
                    index+=1
            else:
                print 'Some issue while writing data to file as records all records are not fetched.'
                
    else:
        print 'Parsing completed'

print 'Total Reviews Collected',len(ReviewList)

#Printing the running time   
print time.clock() - start_time, "seconds"

#Closing the FileReader    
fileReader.close()

#Closing the File Writer
fileWriter.close()
