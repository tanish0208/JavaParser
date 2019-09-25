from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file=open("/home/tanish/Desktop/javadoc/allclasses.html","r")
message=file.read()
soup=BeautifulSoup(message,'html.parser')

a=soup.find_all('a')
length=len(a)

for i in range(len(a)):
    f1=open("/home/tanish/Desktop/javadoc/"+a[i].get('href'),"r")
    mess=f1.read()
    soup = BeautifulSoup(mess, 'html.parser')
    f=open("/home/tanish/"+a[i].get('href').split('.')[0]+".java","w+")
    title=soup.pre
    f.write(title.get_text()+"\n")

    b= (soup.findAll("li",{"class":"blockList"})[2])

    field=b.table.findAll('code')
    count=0
    for i in range(0,len(field),2):
        f.write(field[i].get_text()+" "+field[i+1].get_text()+";"+"\n")
    f.write("\n\n")
    c=soup.findAll("li",{"class":"blockList"})[3]

    cons=c.findAll('code')
    for i in cons:
        f.write(i.get_text()+"\n\n")

    method=soup.find_all("pre", {"class":'methodSignature'})
    for i in range(len(method)):
        f.write(method[i].get_text()+"{\n}\n\n")
    f.close()

