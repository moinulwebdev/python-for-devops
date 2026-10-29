pizza_count = 3
price_per_pizza = 15
total_pizza_cost = float(pizza_count * price_per_pizza)
print(f"Total pizza cost: ${total_pizza_cost}")


soda_cost = 4
total_bill = total_pizza_cost + soda_cost
print(f"Total bill with soda: ${total_bill}")

coupon = 5
final_bill = total_bill - coupon
print(f"Final bill after coupon: ${final_bill}")


friends = 4
cost_per_person = final_bill / friends
print(f"Each person pays: ${cost_per_person}")

total_slices = 24
people_eating = 5
slices_per_person = total_slices // people_eating
print(f"Whole slices per person: {slices_per_person}")


leftover_slices = total_slices % people_eating
print(f"Leftover slices left in the box: {leftover_slices}")  # Output: 4


box_side = 12
box_area = box_side ** 2
print(f"Area of the pizza box base: {box_area} square inches")  # Output: 144


