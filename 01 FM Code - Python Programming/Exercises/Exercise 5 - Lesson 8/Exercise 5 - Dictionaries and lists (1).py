# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "pear", "cherry"]
print(fruits)
# TODO: Add a fruit to the end of the list
fruits.append("strawberry")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "grape")
# TODO: Remove a fruit from the list
fruits.remove("pear")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
number_list = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared
square_numbers = [num ** 2 for num in number_list]
# TODO: Find the sum and average of the original numbers
total_sum = sum(number_list)
average =  total_sum / len(number_list)
# TODO: Print the results
print(f"total sum of numbers: {total_sum}")
print(f"total average of numbers: {average}")
#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = {"Russia":"Moscow",
                      "South Africa":"Pretoria",
                      "Spain":"Madrid"}

print(countries_capitals)
# TODO: Add a new country-capital pair
countries_capitals["Brazil"] = "Brasilia"
# TODO: Update the capital of an existing country
countries_capitals.update({"South Africa": "Cape Town"})
# TODO: Remove a country-capital pair
countries_capitals.pop("Russia")
# TODO: Print the modified dictionary
print(countries_capitals)
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit__colors = {"Orange": "Green",
                 "Banana": "Yellow",
                 "Apple": "Green",
                  "Grape": "Purple"}

# TODO: Print all the fruits (keys)
print(fruit__colors.keys())
# TODO: Print all the colors (values)
print(fruit__colors.values())
# TODO: Print each fruit and its color
print(fruit__colors)
# TODO: Check if a fruit is in the dictionary and print its color
print(fruit__colors.items())