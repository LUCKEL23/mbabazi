#smart study planner
#part A
sessions = []
def add_session():#part b
    subject = input("enter subject: ")
    topic = input("enter topic:")
    date = input("enter date:")

    while True:
        try:
            duration = float(input("enter the duration in minutes"))
            if duration > 0:
                break
            else:
                print("duration must be a positive number")

        except ValueError:
            print("please enter a valid number")

            session = {"subject": subject, "topic" : topic , "date": date ,"duration": duration}
            sessions.append(session)
        #part c
def classify_session(duration):
    if duration < 30:
        return "short"
    elif duration <=90:
        return "medium"
    else:
        return "long"
    #part d
def view_session():
    for session in sessions:
        label = classify_session(session["duration"])
        print(f"{session['subject']:<10}"
            f"{session['topic']:<15}"
            f"{session['date']:<12}")
        #part e
def search_by_subject(subject):
    found = False
    total_duration = 0
    for session in sessions:
        if session["subject"].lower() == subject.lower():
            print(session)
            found = True
            total_duration += session["duration"]
    if not found:
        print("no session found")
    else:
        print(f"total duration:{total_duration} minutes")
                        #part f
def study_statistics():
    total_duration = 0
    subject_totals = {}
    for session in sessions:
        total_duration += session["duration"]
        subject = session["subject"]
        subject_totals[subject] = subject_totals.get(subject,0) + session["duration"]
    total_hours = total_duration / 60
    print(f"total_ study hours: {total_hours}")
    if sessions:
        longest_session = max(sessions,key = lambda session:
                            session["duration"])
        print(f"longest session: {longest_session}")
        #part g
def save_session():
    with open("study_log.txt", "w") as file:
        for session in sessions:
            file.write(str(session) + "\n")
            #part h
def load_sessions():
    try:
        with open("study_log.txt", "r" ) as file:
            for line in file:
                session = eval(line.strip())
                sessions.append(session)
    except FileNotFoundError:
        pass

#part i
def main():
    while True:
        print("\n==== smart study planner ====")
        print("1. add session")
        print("2. view session")
        print("3. search by subject")
        print("4. study statistics")
        print("5. exit")
        choice = input("enter your choice: ")
            
        if choice == "1":
                print("add_session")
        elif choice == "2":
            print("view session")
        elif choice == "3":
                print("search_by_subject")
        elif choice == "4":
            print("study statistics")
        elif choice == "5":
            print("save session")
            break

        else:
            print("invalid choice")
if __name__=="__main__":
    main()


                            





                        

                    
                    
                    
    

                
