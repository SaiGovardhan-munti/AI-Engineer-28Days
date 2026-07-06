scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 60,
    "Frank": 73,
    "Grace": 88
}

Average_score = sum(scores.values())/len(scores.values())
Highest_score = max(scores, key = scores.get)
mininum_score = min(scores, key = scores.get)
Students_above_average = [name for name in scores if scores[name] > Average_score]
count = len(Students_above_average)

print(f"Average score: {round(Average_score, 2)}")
print(f"Highest score: {scores[Highest_score]} ({Highest_score})")
print(f"Lowest score: {scores[mininum_score]} ({mininum_score})")
print(f"Students above average: {Students_above_average}")
print(f"Count above average: {count}")