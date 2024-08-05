#Importing Libraries
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt

#To Read CSV files
confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered = pd.read_csv('time_series_covid19_recovered_global.csv')

#To Drop unwanted columns
confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths = deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
recovered = recovered.drop(['Province/State', 'Lat', 'Long'], axis=1)

#For Taking sum of cases of each country
confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recovered = recovered.groupby(recovered['Country/Region']).aggregate('sum')

#Taking transpose of columns
confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T

#printing variables
p_new_cases = []
p_growth_rate = []
p_active_cases = []
p_overall_growth_rate = []
p_death_rate = []
p_hospitalization_needed = []

#To find number of New Cases in last 15 days
new_cases = confirmed.copy()
#Button in Tkinter window to get the information about number of new cases in India in last 15 days
def myClick1():
    for day in range(1, len(confirmed)):
        new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]
    p_new_cases = new_cases['India'].tail(15)
    #creating Tkinter window for New Cases
    myClick1 = Tk()
    myClick1.title("NEW CASES")
    myClick1.geometry('800x500+200+100')
    myClick1.configure(bg='#046173')
    myClick1.iconbitmap(r'C:\Users\ACER\PycharmProjects\pythonProject1\favicon.ico')
    frame1 = Frame(myClick1, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame1.pack()
    frame1.place(anchor='w', relx=0.14, rely=0.5)
    lableL11 = Label(frame1, text = "The new cases in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL11.pack()
    lableL12 = Label(frame1, text = p_new_cases, font = ("COMIC SANS MS", 10))
    lableL12.pack()

#To find Growth Rate in last 15 days
growth_rate = confirmed.copy()
#Button in Tkinter window to get the information about Growth Rate in India in last 15 days
def myClick2():
    for day in range(1, len(confirmed)):
        growth_rate.iloc[day] = (new_cases.iloc[day] / confirmed.iloc[day - 1]) * 100
    p_growth_rate = growth_rate['India'].tail(15)
    #creating Tkinter window for Growth Rate
    myClick2 = Tk()
    myClick2.title("GROWTH RATE")
    myClick2.geometry('800x500+200+100')
    myClick2.configure(bg='#046173')
    myClick2.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame2 = Frame(myClick2, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame2.pack()
    frame2.place(anchor='w', relx=0.13, rely=0.5)
    lableL21 = Label(frame2, text = "The growth rate in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL21.pack()
    lableL22 = Label(frame2, text = p_growth_rate, font = ("COMIC SANS MS", 10))
    lableL22.pack()

#To find number of Active Cases in last 15 days
active_cases = confirmed.copy()
#Button in Tkinter window to get the information about number of Active cases in India in last 15 days
def myClick3():
    for day in range(0, len(confirmed)):
        active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recovered.iloc[day]
    p_active_cases = active_cases['India'].tail(15)
    #creating Tkinter window for Active Cases
    myClick3 = Tk()
    myClick3.title("ACTIVE CASES")
    myClick3.geometry('800x500+200+100')
    myClick3.configure(bg='#046173')
    myClick3.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame3 = Frame(myClick3, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame3.pack()
    frame3.place(anchor='w', relx=0.125, rely=0.5)
    lableL31 = Label(frame3, text = "The active cases in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL31.pack()
    lableL32 = Label(frame3, text = p_active_cases, font = ("COMIC SANS MS", 10))
    lableL32.pack()

#To find Overall Growth Rate in last 15 days
overall_growth_rate = confirmed.copy()
#Button in Tkinter window to get the information about Overall Growth Rate in India in last 15 days
def myClick4():
    for day in range(1, len(confirmed)):
        overall_growth_rate.iloc[day] = ((active_cases.iloc[day] - active_cases.iloc[day-1]) / active_cases.iloc[day - 1]) * 100
    p_overall_growth_rate = overall_growth_rate['India'].tail(15)
    #creating Tkinter window for Overall Growth Rate
    myClick4 = Tk()
    myClick4.title("OVERALL GROWTH RATE")
    myClick4.geometry('800x500+200+100')
    myClick4.configure(bg='#046173')
    myClick4.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame4 = Frame(myClick4, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame4.pack()
    frame4.place(anchor='w', relx=0.065, rely=0.5)
    lableL41 = Label(frame4, text = "The overall growth rate in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL41.pack()
    lableL42 = Label(frame4, text = p_overall_growth_rate, font = ("COMIC SANS MS", 10))
    lableL42.pack()

#To find Death Rate in last 15 days
death_rate = confirmed.copy()
#Button in Tkinter window to get the information about Death Rate in India in last 15 days
def myClick5():
    for day in range(0, len(confirmed)):
        death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day]) * 100
    p_death_rate = death_rate['India'].tail(15)
    #creating Tkinter window for Death Rate
    myClick5 = Tk()
    myClick5.title("DEATH RATE")
    myClick5.geometry('800x500+200+100')
    myClick5.configure(bg='#046173')
    myClick5.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame5 = Frame(myClick5, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame5.pack()
    frame5.place(anchor='w', relx=0.13, rely=0.5)
    lableL51 = Label(frame5, text = "The death rate in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL51.pack()
    lableL52 = Label(frame5, text = p_death_rate, font = ("COMIC SANS MS", 10))
    lableL52.pack()

#To find number of Hospital Beds required in last 15 days
hospitalization_rate_estimate = 0.05
hospitalization_needed = confirmed.copy()
#Button in Tkinter window to get the information about number of Hospital Beds required in India in last 15 days
def myClick6():
    for day in range(0, len(confirmed)):
        hospitalization_needed.iloc[day] = active_cases.iloc[day] * hospitalization_rate_estimate
    p_hospitalization_needed = hospitalization_needed['India'].tail(15)
    # creating Tkinter window for Hospital Beds
    myClick6 = Tk()
    myClick6.title("HOSPITALIZATION NEEDED")
    myClick6.geometry('800x500+200+100')
    myClick6.configure(bg='#046173')
    myClick6.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame6 = Frame(myClick6, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=5,bg="lightgreen")
    frame6.pack()
    frame6.place(anchor='w', relx=0.045, rely=0.5)
    lableL61 = Label(frame6, text = "The hospitalization needed in India of the last 15 days: ", font = ("COMIC SANS MS", 20))
    lableL61.pack()
    lableL62 = Label(frame6, text = p_hospitalization_needed, font = ("COMIC SANS MS", 10))
    lableL62.pack()

#Visualisation
#To plot the total confirmed cases for multiple countries.
#Button in Tkinter window to get the information about number of new cases in India in last 15 days
def myClick7():
    ax = plt.subplot()
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_title('COVID-19 - Total Confirmed Cases', color='white')
    ax.legend(loc="upper left")
    #Taking List of Countries for which we want to plot the graph of confirmed cases
    countries = ['Austria', 'Italy', 'US', 'Spain', 'China', 'Germany', 'India']
    for country in countries:
        confirmed[country].plot(label = country)
    plt.legend(loc='upper left')
    plt.show()

# To plot actual growth rate of Active cases.
#Button in Tkinter window to get the information about number of new cases in India in last 15 days
def myClick8():
    myClick8 = Tk()
    myClick8.title("ACTUAL GROWTH RATE")
    myClick8.geometry('800x500+200+100')
    myClick8.configure(bg='#046173')
    myClick8.iconbitmap(r'C:\Users\ACER\OneDrive\Desktop\favicon.ico')
    frame8 = Frame(myClick8, width=150, height=100, borderwidth=6, highlightbackground='red', highlightthicknes=5)
    frame8.pack()
    frame8.place(anchor='w', relx=0, rely=0.325)
    lableL81 = Label(frame8, text="Choose country (Italy,Australia,US,China,India,France,Spain):",
                     font=("COMIC SANS MS", 15))
    lableL81.pack()

    #Taking Name of country as input from user for which we want to plot graph for Actual Growth Rate of Active Cases
    entry1 = Entry(myClick8, bd=12, width=32)
    entry1.place(x=280, y=100)
    def datacollect():
        country = entry1.get()
        ax = plt.subplot()
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        plt.subplots_adjust(bottom=0)
        ax.set_title(f'COVID-19 - Actual Growth Rate of Active Cases,{country}', color='white')
        overall_growth_rate[country].plot.bar()
        plt.show()

    button1 = Button(myClick8, text="Submit", command=datacollect, bg="lightblue", fg="blue", height=2, width=35,
                     activebackground="orange")
    button1.place(x=350, y=400)
    button1['font'] = myFont

#Creating Main Tkinter window
root=Tk()
root.title("Track Corona")
root.geometry('800x500+200+100')
root.configure(bg='#046173')
#For changing icon of Tkinter Window
root.iconbitmap(r'C:\Users\ACER\PycharmProjects\pythonProject1\favicon.ico')
#For adding Background image in Tkinter window
img =Image.open(r'C:\Users\ACER\PycharmProjects\pythonProject1\corona_bg.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x = 0,y = 0)
#Creating frame for adding image in Tkinter window
frame = Frame(root, width=150, height=100,borderwidth=6,highlightbackground='red',highlightthicknes=6)
frame.pack()
frame.place(anchor='w', relx=0, rely=0.325)
#adding image
img= (Image.open(r'C:\Users\ACER\PycharmProjects\pythonProject1\corona.jpg'))
#Resize the Image using resize method
resized_image= img.resize((300,205))
new_image= ImageTk.PhotoImage(resized_image)

label = Label(frame, image = new_image)
label.pack()

#Fonts for each Button in Tkinter window
myFont = font.Font(size=8,weight="bold")

#Button1
b1=Button(root,text="NEW CASES",command=myClick1,height=2,width=35,borderwidth=7,bg="lightblue",activebackground="orange")
b1.place(x=350,y=50)
b1['font'] = myFont
#Effect on button
def on_enter(e):
   b1.config(background='grey', foreground= "purple")
def on_leave(e):
   b1.config(background= 'lightblue', foreground= 'blue')
b1.bind('<Enter>', on_enter)
b1.bind('<Leave>', on_leave)

#Button2
b2=Button(root,text="GROWTH RATE",command=myClick2,height=2,width=35,borderwidth=7,bg="lightblue",activebackground="orange")
b2.place(x=350,y=100)
b2['font'] = myFont
#Effect on button
def on_enter(e):
   b2.config(background='grey', foreground= "purple")
def on_leave(e):
   b2.config(background= 'lightblue', foreground= 'blue')
b2.bind('<Enter>', on_enter)
b2.bind('<Leave>', on_leave)

#Button3
b3=Button(root,text="ACTIVE CASES",command=myClick3,height=2,width=35,borderwidth=7,bg="lightblue",activebackground="orange")
b3.place(x=350,y=150)
b3['font'] = myFont
#Effect on button
def on_enter(e):
   b3.config(background='grey', foreground= "purple")
def on_leave(e):
   b3.config(background= 'lightblue', foreground= 'blue')
b3.bind('<Enter>', on_enter)
b3.bind('<Leave>', on_leave)

#Button4
b4=Button(root,text="OVERALL GROWTH RATE",command=myClick4,height=2,width=35,borderwidth=7,bg="lightblue",activebackground="orange")
b4.place(x=350,y=200)
b4['font'] = myFont
#Effect on button
def on_enter(e):
   b4.config(background='grey', foreground= "purple")
def on_leave(e):
   b4.config(background= 'lightblue', foreground= 'blue')
b4.bind('<Enter>', on_enter)
b4.bind('<Leave>', on_leave)

#Button5
b5=Button(root,text="DEATH RATE",command=myClick5,height=2,borderwidth=7,width=35,bg="lightblue",activebackground="orange")
b5.place(x=350,y=250)
b5['font'] = myFont
#Effect on button
def on_enter(e):
   b5.config(background='grey', foreground= "purple")
def on_leave(e):
   b5.config(background= 'lightblue', foreground= 'blue')
b5.bind('<Enter>', on_enter)
b5.bind('<Leave>', on_leave)

#Button6
b6=Button(root,text="HOSPITAL BEDS",command=myClick6,height=2,width=35,bg="lightblue",borderwidth=7,activebackground="orange")
b6.place(x=350,y=300)
b6['font'] = myFont
#Effect on button
def on_enter(e):
   b6.config(background='grey', foreground= "purple")
def on_leave(e):
   b6.config(background= 'lightblue', foreground= 'blue')
b6.bind('<Enter>', on_enter)
b6.bind('<Leave>', on_leave)

#Button7
b7=Button(root,text="COVID-19 - Total Confirmed Cases",command=myClick7,height=2,width=35,borderwidth=7,bg="lightblue",activebackground="orange")
b7.place(x=350,y=350)
b7['font'] = myFont
#Effect on button
def on_enter(e):
   b7.config(background='grey', foreground= "purple")
def on_leave(e):
   b7.config(background= 'lightblue', foreground= 'blue')
b7.bind('<Enter>', on_enter)
b7.bind('<Leave>', on_leave)

#Button8
b8=Button(root,text="Actual Growth rate of Active cases",command=myClick8,height=2,borderwidth=7,width=35,bg="lightblue",activebackground="orange")
b8.place(x=350,y=400)
b8['font'] = myFont
#Effect on button
def on_enter(e):
   b8.config(background='grey', foreground= "purple")
def on_leave(e):
   b8.config(background= 'lightblue', foreground= 'blue')
b8.bind('<Enter>', on_enter)
b8.bind('<Leave>', on_leave)

#Font for Heading
myFont2 = font.Font(size=20,weight="bold")
l=Label(root,text="Analyzing CoronaVirus With Python",font=24,fg="green",bg="lightblue")
l['font'] = myFont2
l.pack()
root.mainloop()