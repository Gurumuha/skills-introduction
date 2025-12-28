#averaging student scores
import math
import time
def calculate_average(numbers):
    return sum(numbers)/ len(numbers)
math_scores =[12, 34, 45, 42, 89, 56, 30, 81, 23, 58, 47]
average =calculate_average(math_scores)
print("The following are grade 6 math results")
time.sleep(1.5)
print(f"The best score was: {max(math_scores)} marks.")
time.sleep(1.5)
print(f"The least score was: {min(math_scores)} marks.")
time.sleep(1.5)
print(f"Average performance was: {average} marks.")
time.sleep(2.5)
if average <=49:
    print("Remark: We need to put more effort in studying math.")
elif average <=69:
    print("Remark: We have a good performance, but there is still room for improvement.")
else:
    print("Remark: This is excellent! Let us keep up the good work!")

