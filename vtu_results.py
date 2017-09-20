#This programs scraps vtu results website and extracts results

import requests
from decimal import Decimal
from bs4 import BeautifulSoup
import operator

dest = r"vturesults.csv"
fw = open(dest, "w")
fw.write("USN,NAME,SGPA"+"\n")



def func(url):
    #word_list =[]
    source_code=requests.get(url).text
    soup = BeautifulSoup(source_code,"lxml")
    try:

        words=soup.find('input',{'id':'txtName'}).get('value')
        word = soup.find('input', {'id': 'txtUSN'}).get('value')
        SGPA = soup.find('span',{'id':'lblSGPA'}).string
        #print(word+"-"+words+"-"+SGPA)



        fw.write(word+","+words+","+SGPA + "\n")
        return Decimal(SGPA)



    except AttributeError:

       """  """








usn = 1
a = 0
c =0
b =0
while(usn<73):
    if (usn<10) :
        a+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs00' + str(usn) + '&sem=2')

    elif (usn<100):
        a+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs0' + str(usn) + '&sem=2')

    else :

        a+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs'+str(usn)+'&sem=2')
    usn +=1

a = a/71


while(usn<153):
    if (usn<10) :
        b+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs00' + str(usn) + '&sem=2')

    elif (usn==80 ):

        b= b

    elif (usn==88):

        b=b

    elif (usn<100):
        b+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs0' + str(usn) + '&sem=2')

    else :

        b+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs'+str(usn)+'&sem=2')
    usn +=1
b = b/79
while(usn<191):
    if (usn<10) :
        c+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs00' + str(usn) + '&sem=2')

    elif (usn<100):
        c+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs0' + str(usn) + '&sem=2')

    elif (usn==171):
        c=c

    else :

        c+=func('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs'+str(usn)+'&sem=2')
    usn +=1

c =c/37
print(a)
print(b)
print(c)
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('username', 'password')

data = [go.Bar(
            x=['CSE-A', 'CSE-B', 'CSE-C'],
            y=[int(a), int(b), int(c)]
    )]

py.plot(data, filename='basic-bar1')
fw.close()

