from fitness import FitnessLog

def main():
    tracker=FitnessLog()
    while True:
        print("<-----Fitness Tracker----->")
        print("1.Log Workout")
        print("2.view All Workouts")
        print("3.Search by Date")
        print("4.search by Exercise")
        print("5.Daily Summary")
        print("6.Weekly summary")
        print("7.Monthly Summary")
        print("8.Most done Exercise")
        print("9.Current Streak")
        print("10.Show Graphs")
        print("11.Exit")

        choice=int(input("Enter your choice between 1 and 11: "))

        if choice==1:
            exercise=input("Enter Exercise Name: ")
            duration=int(input("Enter duration in minutes: "))
            calories=int(input("Enter calories Burned: "))
            date=input("Enter Date(DD-MM-YYYY): ")

            tracker.log_workout(exercise,duration,calories,date)

        elif choice==2:
            tracker.view_all_workouts()    

        elif choice==3:
            date=input("Enter Date(DD-MM-YYYY): ")
            tracker.search_by_date(date)   

        elif choice==4:
            exercise=input("Enter Exercise Name: ")
            tracker.search_by_exercise(exercise) 

        elif choice==5:
            date=input("Enter Date(DD-MM-YYYY): ")
            tracker.daily_summary(date)   

        elif choice==6:
            tracker.weekly_summary()

        elif choice==7:
            mon=input("Enter the Month(MM-YYYY): ")
            tracker.monthly_summary(mon)

        elif choice==8:
            tracker.most_done_exercise()    

        elif choice==9:
            tracker.current_streak()

        elif choice==10:
            tracker.show_graphs()

        elif choice==11:
            print("\nThank you for using Fitness Tracker.....!")
            break

        else:
            print("Invalid choice. Please enter a choice between 1 and 11.")

if __name__=="__main__":
    main()    