User1=input("Enter your name: ")
User2=input("Enter your name: ")
User1_Age=int(input(f"Enter your age {User1}:"))
User2_Age=int(input(f"Enter your age {User2}:"))
if User1_Age > User2_Age:
    print(f"{User1} is older than {User2}")
else:
    print(f"{User2} is older than {User1}")