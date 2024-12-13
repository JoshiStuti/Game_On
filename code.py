from tkinter import *
import pandas as pd

df = pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\idea.csv") #change the address of the file
root = Tk()
root.geometry("500x300")
root.config(bg="yellow") #button func
def page2():


 x=ageval.get()
 print(x)
 y=genderval.get()
 z=categoryval.get()
 root.destroy()
 pg2=Tk()
 pg2.geometry("500x300")
 pg2.title("Game on!!!")
 text= Label(text="Recomendation based on your preferences :",font=("mistral", 25))
 filtered_df= df[(df['Age']==x) & (df['Gender']==y) & (df['Category']==z)]
 game=filtered_df[['Game']]# to get selected columns
 game_splt=game.values.tolist()
 l=[] 
 
 def hyplnk():
  print("hi")
  G=gameval.get()
  print(G)

 import webbrowser
 import pandas as pd



 gamedf = pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\games.csv")  #change the address of the file




 gamefliterdf= gamedf[(gamedf['Game']==G)]
 games=gamefliterdf[['Link']] # to get selected columns
 x=str(games)
 y=x.split(" ")
 z=y[-1]

 z2=str(z)
 print(z2)
# Define the URL you want to link to
 url = z2
# Open the URL in the default web browser
 webbrowser.open(url)




 for i in range(len(game_splt)):
 

  t=(str(game_splt[i][0]))
  l.append(t)

  r=i+1
  print(l)
  gameval= StringVar()
  gameval.set("Choose")




#print(g)
  drop = OptionMenu(pg2, gameval, *l)
  drop.grid(row=1,column=0)
  b= Button(pg2, fg="red", text="GO",command=hyplnk)
  b.grid(row=9 , column= 0)
  text.grid(row=0)



# display
  pg2.mainloop()



#title
root.title("Game on!!!") #label-heading
 
heading1= Label(text="Game On!!! ", fg="red",bg="yellow",font=("mistral", 55))
heading3=Label(text="Best option for video game enthusiasts",bg="yellow",fg="red",font=("mistral", 25))
Age=Label(root, text="Age")
Age.grid(row=5)
gender=Label(root, text="Gender")
gender.grid(row=6)
category=Label(root, text="Gender")
category.grid(row=7)

#age
ageval= StringVar()
ageval.set("Choose")
drop = OptionMenu(root, ageval, "0--5","5--10","10--20","20+")
drop.grid(row=5,column=1)
#gender
genderval= StringVar()
genderval.set("Choose")
drop = OptionMenu(root, genderval, "Male","Female","Neutral")
drop.grid(row=6,column=1)
#category
categoryval= StringVar()
categoryval.set("Choose")
drop=OptionMenu(root,categoryval,"Education","Stimulation","Board Game","Racing","Adventure","Puzzle","Action","Sports")
drop.grid(row=7,column=1)

#button
b1= Button(root,fg="red",text="GO",command=page2)
b1.grid(row=9,column= 1)
heading1.grid(row=0,column=1)
heading3.grid(row=2,column =1)
root.mainloop()
