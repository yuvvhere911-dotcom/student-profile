import matplotlib.pyplot as plt

# Tere skills
skills = ['HTML', 'CSS', 'Python', 'Git', 'AI']
marks = [90, 85, 80, 75, 88]

plt.figure(figsize=(8,5))
plt.bar(skills, marks, color='skyblue')
plt.title('My Skills Chart - Amity Agile Lab')
plt.xlabel('Skills')
plt.ylabel('Marks %')
plt.ylim(0, 100)

# Chart ko image me save karo
plt.savefig('chart.png')
print("chart.png ban gayi!")




















