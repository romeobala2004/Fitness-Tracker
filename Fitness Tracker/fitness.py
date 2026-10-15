import pandas as pd
import os
from datetime import datetime, timedelta
from collections import Counter
import matplotlib.pyplot as plt

class Workout:

    def __init__(self, exercise, duration, calories, date):
        self.exercise=exercise
        self.duration=duration
        self.calories=calories
        self.date=date

class FitnessLog:

    def __init__(self):
        self.file_name="fitness_data.csv"
        if not os.path.exists(self.file_name):
            df=pd.DataFrame(columns=["Exercise","Duration","Calories","Date"])
            df.to_csv(self.filename, index=False)

    def log_workout(self,exercise,duration,calories,date):
        workout=Workout(exercise,duration,calories,date)
        df=pd.read_csv(self.file_name)
        new_row=pd.DataFrame({"Exercise":[workout.exercise],"Duration":[workout.duration],"Calories":[workout.calories],"Date":[workout.date]})  
        df=pd.concat([df,new_row],ignore_index=True) 
        df.to_csv(self.file_name, index=False)
        print("Workout Added Successfully...")

    def view_all_workouts(self):
        df=pd.read_csv(self.file_name)

        if df.empty:
            print("No workout records Found")
        else:
            print(df)               

    def search_by_date(self,date):
        df=pd.read_csv(self.file_name)
        result=df[df["Date"]==date]    

        if result.empty:
            print("No records Found")
        else:
            print(result)    

    def search_by_exercise(self,exercise):
        df=pd.read_csv(self.file_name)
        result=df[df["Exercise"].str.lower()==exercise.lower()]

        if result.empty:
            print("No records Found")
        else :
            print(result)

    def daily_summary(self,date):
        df=pd.read_csv(self.file_name)
        result=df[df["Date"]==date]

        if result.empty:
            print("No records Found")    
        else:
            print("Daily Summary")
            print("Total Workouts: ",len(result))
            print("Total Calories: ",result["Calories"].sum()) 
            print("Total Duration: ",result["Duration"].sum())  
               

    def weekly_summary(self):
        df=pd.read_csv(self.file_name)

        if df.empty:
            print("No records Found")
        else:
            df["Date"]=pd.to_datetime(df["Date"],format="%d-%m-%Y")
            today=datetime.today()
            week=today-timedelta(days=7)
            print("Weekly Summary")
            result=df[df["Date"]>=week]
            print("Total Workouts: ",len(result))
            print("Total Calories: ",result["Calories"].sum()) 
            print("Total Duration: ",result["Duration"].sum()," minutes")

    def monthly_summary(self,mon):
        df=pd.read_csv(self.file_name)
        Month,Year=mon.split("-")
        Month=int(Month)
        Year=int(Year)
        df["Date"]=pd.to_datetime(df["Date"],format="%d-%m-%Y")
        result=df[(df["Date"].dt.month==Month) & (df["Date"].dt.year==Year)]

        if result.empty:
            print("No records Found")
        else:
            print("Monthly Summary")
            print("Total Workouts: ",len(result))
            print("Total Calories: ",result["Calories"].sum()) 
            print("Total Duration: ",result["Duration"].sum()," minutes")

    def most_done_exercise(self):
        df=pd.read_csv(self.file_name)

        if df.empty:
            print("No records Found")
        else:
            counter=Counter(df["Exercise"])
            exercise=counter.most_common(1)[0]
            print("Most done exercise: ",exercise[0])
            print("Times Performed: ",exercise[1])

    def current_streak(self):
        df=pd.read_csv(self.file_name)

        if df.empty:
            print("Current Streak: 0 days")
        else:
            dates=sorted(set(pd.to_datetime(df["Date"],format="%d-%m-%Y").dt.date),reverse=True)
            streak=1
            for i in range(len(dates)-1):
                if dates[i]-dates[i+1]==timedelta(days=1):
                    streak+=1
                else:
                    break
            print("Current Streak: ",streak,"days")

    def show_graphs(self):
        df=pd.read_csv(self.file_name)

        if df.empty:
            print("No data to plot")
        else:
            df["Date"]=pd.to_datetime(df["Date"],format="%d-%m-%Y")

            plt.figure(figsize=(8,5))
            plt.plot(df["Date"],df["Calories"],marker="o")
            plt.title("Calories Burned over time")
            plt.xlabel("Date")
            plt.ylabel("Calories")
            plt.grid(True)
            plt.show()  


            exercise_count=df["Exercise"].value_counts()
            plt.figure(figsize=(8,5))
            exercise_count.plot(kind="bar")
            plt.title("Exercise Frequency")
            plt.xlabel("Exercise")
            plt.ylabel("count")
            plt.show()                 
