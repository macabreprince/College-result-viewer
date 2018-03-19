import sqlite3
import re
from robobrowser import RoboBrowser
def f(id):
    br = RoboBrowser( history=True,parser='html.parser')
    br.open('http://www.bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx')
    form = br.get_form( )
    form["ctl00$ContentPlaceHolder1$ddlAcademicSession"].value = '2017-2018'

    form['ctl00$ContentPlaceHolder1$ddlSem'].value = '3'
    form['ctl00$ContentPlaceHolder1$ddlResultCategory'].value='R'
    form['ctl00$ContentPlaceHolder1$txtRollno'].value=id

    html=br.submit_form(form)
    src=str(br.parsed())

    m=re.search('<span id="ctl00_ContentPlaceHolder1_omk">',src)
    if m==None:
        return None
    t=m.end()
    newstring=src[t:t+3]

    f=int(newstring)
    f=f/10
    return str(f)
id=1604310001
t=0
while t<60:
    t=t+1
    id=id+1
    l=f(id)
    if l!=None:
         print(str(id)+"   Percentage is : "+l)

 
