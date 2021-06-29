names = input().split()
assignments = list(map(int, input().split()))
grades = list(map(int, input().split()))

number_of_students = len(names)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(number_of_students):
    print(message.format(names[i], assignments[i], grades[i], grades[i] + (2 * assignments[i])))
