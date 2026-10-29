# pizza_count = 3
# price_per_pizza = 15
# total_pizza_cost = float(pizza_count * price_per_pizza)
# print(f"Total pizza cost: ${total_pizza_cost}")


# soda_cost = 4
# total_bill = total_pizza_cost + soda_cost
# print(f"Total bill with soda: ${total_bill}")

# coupon = 5
# final_bill = total_bill - coupon
# print(f"Final bill after coupon: ${final_bill}")


# friends = 4
# cost_per_person = final_bill / friends
# print(f"Each person pays: ${cost_per_person}")

# total_slices = 24
# people_eating = 5
# slices_per_person = total_slices // people_eating
# print(f"Whole slices per person: {slices_per_person}")


# leftover_slices = total_slices % people_eating
# print(f"Leftover slices left in the box: {leftover_slices}")  # Output: 4


# box_side = 12
# box_area = box_side ** 2
# print(f"Area of the pizza box base: {box_area} square inches")  # Output: 144


# movie_ticket_price = 12
# minimum_age = 18

# customer_age = 20
# customer_cash = 12

# # result = customer_age > minimum_age
# # result = customer_cash >= movie_ticket_price
# # result = customer_cash == movie_ticket_price
# # result = customer_age != minimum_age
# # result = customer_age > 17
# result = customer_age >= minimum_age

age = 12
# has_kids = True
# is_adult = age >= 18

# if is_adult:
#     result = "Survey access granted."
# else:
#     result = "Access denied: Must be 18 or older."

# print(result)

# if age < 4:
#     print("Ticket is free for toddlers!")

# elif age <= 12:
#     print("Child ticket price: $8.00")

# elif age < 65:
#     print("Adult ticket price: $15.00")

# else:
#     print("Senior citizen ticket price: $10.00")

# not_married = True
# age = 10

# if not_married == True and age >= 18:
#     print("Most elligible bachelor getting married")
# else:
#     print("Papa will....")

# has_job = False
# age = 30
# if has_job == True or age >= 18:
#     print("Most elligible bachelor getting married")
# else:
#     print("Okormar dheki, bia korte asche, maira...")


bangla = int(input("Enter your Bangla mark : "))
english = int(input("Enter your English mark : "))
math = int(input("Enter your Math mark : "))
science = int(input("Enter your Science mark : "))
bgs = int(input("Enter your BGS mark : "))
islam = int(input("Enter your Islam mark : "))

if (bangla < 0 or bangla > 100 or english < 0 or english > 100 or math < 0 or math > 100 or science < 0 or science > 100 or bgs < 0 or bgs > 100 or islam < 0 or islam > 100):
    result = "Invalid mark! Mark must be between 0 and 100."
else:
    total_mark = bangla + english + math + science + bgs + islam
    average = total_mark / 6

    if average >= 80 and average <= 100:
        grade = "A+"
    elif average >= 70 and average <= 79:
        grade = "A"
    elif average >= 60 and average <= 69:
        grade = "A-"
    elif average >= 50 and average <= 59:
        grade = "B"
    elif average >= 40 and average <= 49:
        grade = "C"
    else:
        grade = "F"

    if bangla >= 40 and english >= 40 and math >= 40 and science >= 40 and bgs >= 40 and islam >= 40:
        result = "Passed"
    else:
        result = "Failed"
        grade = "F"

    print("\n--------Result--------")
    print(f"Grade : {grade}")
    print(f"Total mark : {total_mark}")
    print(f"Average mark : {average}")

print(result)