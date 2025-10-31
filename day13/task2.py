from datetime import date, datetime

print("🎂 Birthday Calculator 🎂")

birth = input("Enter your birth date (YYYY-MM-DD): ")
bday = datetime.strptime(birth, "%Y-%m-%d").date()
today = date.today()

days_lived = (today - bday).days
years = days_lived // 365


weekday = bday.strftime("%A")




next_bday = bday.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year + 1)
days_to_bday = (next_bday - today).days


zodiac = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat"][bday.year % 12]
birthstone = ["Garnet","Amethyst","Aquamarine","Diamond","Emerald","Pearl","Ruby","Peridot","Sapphire","Opal","Topaz","Turquoise"][bday.month - 1]

print("\n🎉 Birthday Facts:")
print(f"You were born on a {weekday}")
print(f"You are {years} years old")
print(f"You have lived for {days_lived} days")
print(f"Your next birthday is in {days_to_bday} days")
print(f"You were born in the year of the {zodiac}")
print(f"Your birthstone is {birthstone}")
