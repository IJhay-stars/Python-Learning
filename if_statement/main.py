# the if statement controls the program flow. Python has 3 control flow: if, elif and else....abs

user_role = input("Please input role name: ")
is_authenticated = True

if is_authenticated and user_role == "Admin":
    print("Full System Access Granted!")
elif is_authenticated and user_role == "Editor":
    print("Limited Access Granted")
else:
    print("Access denied!")
    
##Exercises

## Write a script that accepts a numeric grade (0-100) and prints the corresponding letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60).

def get_score_grade(score:float) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
if __name__ == "__main__":
    try:
        score_input = float(input("Please enter a numrical rating: "))
        if 0 <= score_input <= 100:
            print(f"Letter Grade: {get_score_grade(score_input)}")
        else:
            print("Please, enter a valid numerical rating from 1-100")
    except ValueError:
        print("Invalid Input. Please, enter a numerical value")