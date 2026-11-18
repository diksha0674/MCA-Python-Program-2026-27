# Q4. Tuples, sets and set operations

roll_numbers = (101, 102, 103, 104)
print("Tuple:", roll_numbers)
print("Tuple elements:")
for roll in roll_numbers:
    print(roll)
print("Indexing:", roll_numbers[0])
print("Slicing:", roll_numbers[1:3])
print("Concatenation:", roll_numbers + (105, 106))

course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}
print("\nCourse A:", course_a)
print("Course B:", course_b)
print("Union:", course_a | course_b)
print("Intersection:", course_a & course_b)
print("Difference (A - B):", course_a - course_b)
print("Symmetric difference:", course_a ^ course_b)
print("Is A subset of B?", course_a.issubset(course_b))
print("Is A superset of B?", course_a.issuperset(course_b))

course_a.add(107)
course_a.discard(101)
print("After adding 107 and removing 101:", course_a)

even_squares = {x * x for x in range(1, 11) if x % 2 == 0}
print("Squares of even numbers from 1 to 10:", even_squares)
