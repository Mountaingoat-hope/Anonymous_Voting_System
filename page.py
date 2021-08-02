import sys
import psycopg2
import csv
from flask import Flask,render_template,request
import psycopg2

app=Flask("Vote")


@app.route("/")
def base():
  dbconn=psycopg2.connect("dbname=Votepool")
  cursor=dbconn.cursor()
  fname=sys.argv[1]
  f=open(fname)
  reader=csv.reader(f)
  el=[]
  li=[]
  for title,purpose,expiry in reader:
    el.append(title)
    el.append(purpose)
    el.append(int(expiry))
    li.append(el)
    el=[]
  
  h='''cursor.execute("SELECT name,username,pw FROM Auth")
  for name,username,password in cursor.fetchall():
       tu.append(name)
       tu.append(username)
       tu.append(password)
       li.append(tu)
  dbconn.commit()'''
  
  user_votelist=["Students","Elective course","Branch represenative"]
  return render_template("page.html",user_votelist=li)



def main():
   fname=sys.argv[1]
   #insert(fname)
   dump(fname)
   
#main()

if __name__=="__main__":
   #print("main is called")
   app.run()
   
else:
   print("main not called")
   addit()

