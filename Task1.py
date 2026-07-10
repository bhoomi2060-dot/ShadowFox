# Task 1
#Question 1. Variables

# (i) 
pi=22/7
print(type(pi))

#(ii)
#for=4
#print(for)
#Reason : The reason is that for is a reserved keyword in Python

#(iii)
p=1000
r=5
t=3
Simple_Interest=(p*r*t)/100
print("Principal Amount:", p)
print("Rate of Interest:", r, "%")
print("Time Period:", t, "years")
print(Simple_Interest)


#Question 2. Numbers
#(i)
def format_values(number, representation):
    # The format function uses the representation character ('o') to format the number
    # The string format syntax f"{number:{representation}}" evaluates to f"{145:o}"
    return f"{number:{representation}}"

# Call the function with 145 and 'o'
result = format_values(145, 'o')

# Print the final result
print("Formatted Result:", result)

#(ii)
radius = 84
pi = 3.14
water_per_sq_meter = 1.4
pond_area = pi * (radius ** 2)
total_water = pond_area * water_per_sq_meter
print("Pond Area:", pond_area, "square meters")
print("Total Water in the Pond:", int(total_water), "liters")

#(iii)
distance = 490
time= 7*60
speed=distance//time
print("Speed :", speed, ",miles per hour")

#Question 3 If Condition
#(i)
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi=weight/(height**2)
if(bmi>=30):
    print("Obese")
elif(bmi>=25 and bmi<=29):
    print("Overweight")
elif(bmi>=18.25):
    print("Normal")
else:
    print("Underweight")

#(ii)
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city=input("Enter the name of the city:")
if city in Australia:
    print(city,"City is Australia")
elif city in UAE:
    print(city,"City is in UAE")
elif city in India:
    print(city,"City is in India")
else:
    print("City not found ")

#(iii)
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = find_country(city1)
country2 = find_country(city2)

if country1 is None or country2 is None:
    print("One or both cities were not found in the list")
elif country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")

#Question 4 Lists
justice_league=["Superman","Batman","Wonderwoman","Aquaman","Frash","Green Lantern"]
#(i)
print(len(justice_league))

#(ii)
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

#(iii)
justice_league.remove("Wonderwoman")
justice_league.insert(0,"Wonderwoman")

#(iv)
justice_league.remove("Superman")
aquaman_index=justice_league.index("Aquaman")
justice_league.insert(aquaman_index+1,"Superman")
print(justice_league)

#(v)
justice_league=["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print("New justice league :",justice_league)

#(vi)
justice_league.sort()
print("Sorted list",justice_league)

#Question 5. Dictonary
# (i)
friends = ["Rahul", "Priya", "Aditya", "Neha", "Rohan"]
friend_tuples = []

for name in friends:
    friend_tuples.append((name, len(name)))

print("Friends List:")
print(friends)

print("\nList of Tuples (Name, Length):")
print(friend_tuples)

#(ii)
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}


your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: ${your_total}")
print(f"Partner's total expenses: ${partner_total}")
if your_total > partner_total:
    print(f"You spent more overall, by ${your_total - partner_total}")
elif partner_total > your_total:
    print(f"Partner spent more overall, by ${partner_total - your_total}")
else:
    print("You both spent the same amount overall")
biggest_diff_category = None
biggest_diff = 0

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > biggest_diff:
        biggest_diff = diff
        biggest_diff_category = category

print(f"\nBiggest difference in spending: {biggest_diff_category}, difference of ${biggest_diff}")