print("Welcome to tip calculator!")

bill = int(input("Enter the bill amount :\n$"))
tip = int(input("Enter the tip percentage :\nPercentage : "))
split = int(input("Enter the number of people :\nPeople : "))

total = ("{:.2f}".format((bill * (tip / 100) + bill) / split))

print(f"Each person should pay : ${total}")