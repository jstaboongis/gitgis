import urllib2
import cookielib
import os

global listurls
listurls = ["https://www.wunderground.com/weather/us/ca/anaheim",
        "https://www.wunderground.com/weather/us/ca/burbank",
        "https://www.wunderground.com/weather/us/ca/corona",
        "https://www.wunderground.com/weather/us/ca/indio",
        "https://www.wunderground.com/weather/us/ca/long-beach",
        "https://www.wunderground.com/weather/us/ca/los-angeles",
        "https://www.wunderground.com/weather/us/ca/newport-beach",
        "https://www.wunderground.com/weather/us/ca/oceanside",
        "https://www.wunderground.com/weather/us/ca/oxnard",
        "https://www.wunderground.com/weather/us/ca/pasadena",
        "https://www.wunderground.com/weather/us/ca/redlands",
        "https://www.wunderground.com/weather/us/ca/riverside",
        "https://www.wunderground.com/weather/us/ca/san-diego",
        "https://www.wunderground.com/weather/us/ca/santa-barbara",
        "https://www.wunderground.com/weather/us/ca/santa-clarita",
        "https://www.wunderground.com/weather/us/ca/santa-monica",
        "https://www.wunderground.com/weather/us/ca/simi-valley",
        "https://www.wunderground.com/weather/us/ca/temecula",
        "https://www.wunderground.com/weather/us/ca/upland"]

global listurls2
listurls2 = ["https://www.wunderground.com/weather/us/ca/anaheim",
        "https://www.wunderground.com/weather/us/ca/burbank",
        "https://www.wunderground.com/weather/us/ca/corona",
        "https://www.wunderground.com/weather/us/ca/indio",
        "https://www.wunderground.com/weather/us/ca/long-beach",
        "https://www.wunderground.com/weather/us/ca/los-angeles",
        "https://www.wunderground.com/weather/us/ca/newport-beach",
        "https://www.wunderground.com/weather/us/ca/oceanside",
        "https://www.wunderground.com/weather/us/ca/oxnard",
        "https://www.wunderground.com/weather/us/ca/pasadena",
        "https://www.wunderground.com/weather/us/ca/redlands",
        "https://www.wunderground.com/weather/us/ca/riverside",
        "https://www.wunderground.com/weather/us/ca/san-diego",
        "https://www.wunderground.com/weather/us/ca/santa-barbara",
        "https://www.wunderground.com/weather/us/ca/santa-clarita",
        "https://www.wunderground.com/weather/us/ca/santa-monica",
        "https://www.wunderground.com/weather/us/ca/simi-valley",
        "https://www.wunderground.com/weather/us/ca/temecula",
        "https://www.wunderground.com/weather/us/ca/upland"]


listnumbers = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']



def GetWeather(wurl, urls):
    
    cookieJar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    
    request = urllib2.Request(wurl)
    page = opener.open(request)

    # This is one big string
    rawdata = page.read()

    # This breaks it up into lines
    lines_of_data = rawdata.split('\n')

    # This is one line in the raw data that looks interesing.  I'm going to
    # filter the raw data based on the "og:title" text.
    #
    #'<meta name="og:title" content="Beijing, Beijing | 31&deg; | Clear" />

    # The "if line.find(" bit is the filter.
    special_lines = [line for line in lines_of_data if line.find('og:title')>-1]
    #print special_lines

    # Now we clean up - this is very crude, but you can improve it with
    # exactly what you want to do.
    info = special_lines[0].replace('"','').split('content=')[1]
    sections = info.split('|')
    #print sections
    try:
        city = sections[0]
        
        temp = sections[1]
        temp = temp.replace(" ' ","")
        temp = temp.replace("&deg;","")
        
        weather = sections[2]
        weather = weather.replace(" />","")
        print city + temp + weather
        num = listurls2.index( i )
        listurls.remove(i)
        listnumbers[num] = temp


    except:
        print 'nope'

while listurls != []:
    for i in listurls:
        GetWeather(i, listurls)


os.remove('C:\Users\WORK\Documents\GitHub\gitgis\sampleout.csv')
fr = open('C:\Users\WORK\Documents\GitHub\gitgis\samplenoweather.csv','r')
fw = open('C:\Users\WORK\Documents\GitHub\gitgis\sampleout.csv','w')
line = fr.readline()
line = line.replace('\n','')
fw.write(line + ", Temp\n")
count = 0
while line:
    line = fr.readline()
    line = line.replace('\n','')

    
    fw.write(line + ', ' + listnumbers[count] + '\n')
    count = count + 1
    if count == 19:
        break
         
         
fr.close()
fw.close()
