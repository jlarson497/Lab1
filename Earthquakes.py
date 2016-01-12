import json
from urllib.request import urlopen


month = input("Enter the month in numeric format (MM): ")
year = input("Enter the year (YYYY): ")
url = "http://www.seismi.org/api/eqs/{0}/{1}".format(month, year)

response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)

print(data["earthquakes"])

#newcommit
#    region = earthquake.GET("Region")
#    regionList.append(region)
#print(regionList)




