import sys
import psycopg2
import csv
from flask import Flask,render_template,request

app=Flask("Vote")


@app.route("/")
def base():
  return render_template("base.html")

@app.route("/insert")
def insert(fname):
   dbconn=psycopg2.connect("dbname=Votepool")
   cursor=dbconn.cursor()
   f=open(fname)
   reader=csv.reader(f)
   
   for name,username,password in reader:
      cursor.execute("Insert into Auth(name, username, pw) Values (%s, %s, %s)",(name, username, password))
   dbconn.commit()
   #print("Successfully committed")
   f.close()

@app.route("/dump")
def dump(fname):
   dbconn=psycopg2.connect("dbname=Votepool")
   cursor=dbconn.cursor()
   f=open(fname, "w")
   writer=csv.writer(f)
   
   cursor.execute("SELECT name,username,pw FROM Auth WHERE id=3")
   for name,username,password in cursor.fetchall():
     print(name, username,   password)
   dbconn.commit()
   #print("Successfully selected")
   f.close()
   
def main():
   fname=sys.argv[1]
   #insert(fname)
   dump(fname)
   
#main()
def addit():
   x=3
   y=4
   print("added addition complete")
   return x+y

if __name__=="__main__":
   #print("main is called")
   app.run()
   
else:
   print("main not called")
   addit()

