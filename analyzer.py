target_skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "SQL",
    "Pandas",
    "NumPy",
    "Data Visualization",
    "Statistics"
]

with open("resume.txt", "r") as file:
    resume_content = file.read()

resume_content = resume_content.lower()

matched_skills = []
missing_skills = []

for skill in target_skills:
    if skill.lower() in resume_content:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

match_score = (len(matched_skills) / len(target_skills)) * 100

print("----- Resume Analysis -----")
print(f"Match Score: {match_score:.2f}%")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nSkills to Improve:")
for skill in missing_skills:
    print("-", skill)
