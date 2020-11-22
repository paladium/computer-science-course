# First programme
'''a = ["Physics", "Math", "Chemistry", "Biology", "Astronomy", "Informatics", "Math", "Physics"]
without_duplicates = []
for subject in a:
  if subject not in without_duplicates:
    without_duplicates.append(subject)
a = without_duplicates
print(a)'''
#Correct
# Second programme
'''real_planets = ["Earth", "Neptun", "Mars", "Saturn"]
star_wars = ["Tatooine", "Naboo", "Mustafar", "Kamino"]
joined = real_planets + star_wars
joined.sort(reverse=True)
print(joined)'''
#Correct
# Third programme
'''phone_brands = ["Samsung", "Apple", "Huawei", "Xiaomi", "HTC", "OnePlus"]
laptop_brands = ["Apple", "MSI", "Samsung", "HP", "ASUS"]
common_brands = []
for brand in phone_brands:
  if brand in laptop_brands:
    common_brands.append(brand)
print(common_brands)'''
#Correct

# Fourth programme
'''a = int(input("Please , enter the number : "))
b = int(input("Enter the second number : "))
new_list = []
for num in range(a, b+1):
  new_list.append(num)
print(new_list)'''
#Correct

# Fifth programnumbers 
numbers = [3, 6, 21, 2, 96.55, 11, 100.5]
sum_num = 0
for number in numbers:
  sum_num += number
print(sum_num)
#Correct