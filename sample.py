import urllib2
import cookielib


list1 = ["https://www.wunderground.com/weather/us/ca/anaheim",
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

list2 = []


def GetWeather(wurl,listincomplete,listcomplete,run):
    
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
        weather = sections[2]
        print city + temp + weather
        if run == 'true':
            listincomplete.remove(i)
        index = listcomplete.index(i)
        listcomplete[index] = str(temp) + str(weather)
    except:
        listincomplete.append(i)

for i in list1:
    GetWeather(i, list2, list1, 'false')

while list2 != []:
    for i in list2:
        GetWeather(i, list2, list1, 'true')
            

print list1
