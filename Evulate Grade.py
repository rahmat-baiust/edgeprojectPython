# Function to determine the grade based on the percentage
def determine_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Input from user with validation
while True:
    try:
        percentage = float(input("Enter the percentage: "))
        
        if 0 <= percentage <= 100:  # Check if the input is a valid percentage
            grade = determine_grade(percentage)
            print(f"The grade for {percentage}% is: {grade}")
            break
        else:
            print("Please enter a valid percentage between 0 and 100.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the percentage.")
