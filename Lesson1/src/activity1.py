import sys

scores = []

num_students = int(input("How many students? "))

for i in range(num_students):
    score = float(input(f"Enter score for Student {i + 1}: "))
    scores.append(score)

print()
print("Student Scores:")
for score in scores:
    print(score)
print()

passed_count = 0
failed_count = 0

for i in range(len(scores)):
    score = scores[i]

    if score >= 90:
        remark = "Excellent"
    elif score >= 80:
        remark = "Very Good"
    elif score >= 75:
        remark = "Good"
    else:
        remark = "Failed"

    if score >= 75:
        status = "Passed"
        passed_count = passed_count + 1
        print(f"Student {i + 1}: {score} - {remark} - {status}")
    else:
        failed_count = failed_count + 1
        print(f"Student {i + 1}: {score} - {remark}")

print()
print("Total Score:", sum(scores))
print("Average Score:", sum(scores) / len(scores))
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Passed:", passed_count)
print("Failed:", failed_count)