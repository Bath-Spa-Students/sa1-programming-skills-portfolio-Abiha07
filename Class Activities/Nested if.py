monthly_salary = int(input("Enter your monthly salary: "))

if monthly_salary >= 14000:
    years_on_job = float(input("Enter your experience in years on the job: "))
    
    if years_on_job >= 2:
        print("You are qualified for your job.")
    else:
        print("Your experience is less than 2 years.")
else:
    print("You should earn at least 14000 to qualify.") 
