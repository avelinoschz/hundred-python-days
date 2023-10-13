#1. Create a greeting for your program.
print("Will create an awesome band name for you.")

#2. Ask the user for the city that they grew up in.
# Tried two different approaches to test new lines + input 
print("What's your hometown name?")
hometown_name = input()

#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = hometown_name + " " + pet_name

#5. Make sure the input cursor shows on a new line:
print("Your new band's name is: " + band_name)

# Solution: https://replit.com/@appbrewery/band-name-generator-end