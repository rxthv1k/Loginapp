def __init__(self, name):
        self.name = name
        self.votes = 0




candidates=[]




def pwd():
    global x
    x=False
    global pswd
    pswd=input("Enter password: ")
    if pswd.upper()=='VGSELECTIONS123':
        print("Access granted")
        x=True
    else:
        print("Incorrect password")



def changepassword():
    cp=input("Enter current password: ")
    pswd="vgselections123"
    if cp.upper() == pswd :
        pswd=input("Enter new password: ")

        if pswd == cp :
            print("Use a password you haven't used before")
        else:
            print("Password changed successfully")

    else:
        print("Current password is wrong")









def add_candidate(candidates, name):
    candidates.append(name)
    print(f"{name} has been added as a candidate.")


def add_candidateButton():
    pwd()
    if x == True:
        name = input("Enter candidate name: ")
        add_candidate(candidates, name)










def cast_vote(candidates, candidate_name):
    for candidate in candidates:
        if candidate.name == candidate_name:
            candidate.votes += 1
            print(f"Vote for {candidate_name} has been recorded.")
            return
    print(f"Error: Candidate {candidate_name} not found!")


def cast_voteButton():
    candidate_name = input("Enter candidate name to cast vote: ")
    cast_vote(candidates, candidate_name)









def display_candidates(candidates):
    print("List of candidates:")
    for candidate in candidates:
        print(f"{candidate.name}")

def display_candidatesButton():
    pwd()
    if x == True:
        display_candidates(candidates)

    elif choice == "4":
        pwd()
        if x == True:
            winner = get_winner(candidates)
            if winner:
                print(f"The winner is: {winner.name} with {winner.votes} votes!")
            else:
                print("No winner yet.")









def get_winner(candidates):
    if not candidates:
        return None
    winner = max(candidates, key=lambda x: x.votes)
    return winner

def get_winnerButton():
    pwd()
    if x == True:
        winner = get_winner(candidates)
        if winner:
            print(f"The winner is: {winner.name} with {winner.votes} votes!")
        else:
            print("No winner yet.")









def ExitButton():
    pwd()
    if x == True:
        print("Exiting the program.")









def main():
    candidates = []

    while True:
        print("\n===== School Headboy Election =====")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. Display Candidates")
        print("4. Get Winner")
        print("5. Exit")
        print("6. Change Password")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_candidateButton()
        elif choice == "2":
            cast_voteButton()
        elif choice == "3":
            display_candidatesButton()
        elif choice == "4":
            get_winnerButton()
        elif choice == "5":
            ExitButton()
        elif choice== "6":
            changepassword()
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

























class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0


def pwd():
    global x
    x = False
    global pswd
    pswd = input("Enter password: ")
    if pswd.upper() == 'VGSELECTIONS123':
        print("Access granted")
        x = True
    else:
        print("Incorrect password")


def changepassword():
    cp = input("Enter current password: ")
    pswd = "vgselections123"
    if cp.upper() == pswd:
        pswd = input("Enter new password: ")

        if pswd == cp:
            print("Use a password you haven't used before")
        else:
            print("Password changed successfully")

    else:
        print("Current password is wrong")




#User Defined functions specifically for the program

def add_candidate(candidates, name):
    candidates.append(Candidate(name))
    print(f"{name} has been added as a candidate.")

def add_candidatefinal():
    pwd()
    if x == True:
        name = input("Enter candidate name: ")
        add_candidate(candidates, name)

def cast_vote(candidates, candidate_name):
    for candidate in candidates:
        if candidate.name == candidate_name:
            candidate.votes += 1
            print(f"Vote for {candidate_name} has been recorded.")
            return
    print(f"Error: Candidate {candidate_name} not found!")

def display_candidates(candidates):
    print("List of candidates:")
    for candidate in candidates:
        print(f"{candidate.name}")

def get_winner(candidates):
    if not candidates:
        return None
    winner = max(candidates, key=lambda x: x.votes)
    return winner




def main():
    candidates = []

    while True:
        print("\n===== School Headboy Election =====")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. Display Candidates")
        print("4. Get Winner")
        print("5. Exit")
        print("6. Change Password")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            pwd()
            if x == True:
                name = input("Enter candidate name: ")
                add_candidate(candidates, name)
        elif choice == "2":
            candidate_name = input("Enter candidate name to cast vote: ")
            cast_vote(candidates, candidate_name)
        elif choice == "3":
            pwd()
            if x==True:
                display_candidates(candidates)
        elif choice == "4":
            pwd()
            if x==True:
                winner = get_winner(candidates)
                if winner:
                    print(f"The winner is: {winner.name} with {winner.votes} votes!")
                else:
                    print("No winner yet.")
        elif choice == "5":
            pwd()
            if x==True:
                print("Exiting the program.")
                break
        elif choice== "6":
            changepassword()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

