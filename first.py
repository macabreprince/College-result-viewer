import re
import urllib.request
url = "https://en.wikipedia.org/wiki/"
country = input("Enter your country")
#country="India"
url = url + country
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('<th scope="row">Capital', data1)
start = m.start()
newend = start + 150
allnewstring = data1[start:newend]
index = allnewstring.find("title=")
index = index + 6
newend = allnewstring.find("</a>")
verynew = allnewstring[index:newend]
verynewindex = verynew.find(">")
final = verynew[index:verynewindex]
final = verynew[0:verynewindex]
print("The Capital of "+ country+ " is "+final )


#print(final)