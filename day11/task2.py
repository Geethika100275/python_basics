
file_name = "file.txt"

try:
    with open(file_name, "r") as f:
        scores = [line.strip().split(":") for line in f if line.strip()]
        scores = [(name.strip(), int(score.strip())) for name, score in scores]
except FileNotFoundError:
    scores = []
print("High Scores Tracker")
print("Current high scores:")
for name, score in scores:
    print(f"{name}: {score}")
name = input("Enter your name: ")
score = int(input("Enter your score: "))
scores.append((name, score))
scores.sort(key=lambda x: x[1], reverse=True)
with open(file_name, "w") as f:
    for name, score in scores:
        f.write(f"{name}: {score}\n")
print("Score saved!")
print("Updated high scores:")
for name, score in scores:
    print(f"{name}: {score}")
