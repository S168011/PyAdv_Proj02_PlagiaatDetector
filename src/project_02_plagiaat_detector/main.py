from pathlib import Path
lazy import jinja2 as jinja

StudentA = [
    "aray",
    "pithon",
    "recieve",
    "definately",
    "seperate",
    "teh",
    "occured"
]

StudentB = [
    "aray",
    "pithon",
    "definately",
    "enviroment",
    "wich",
    "untill",
    "succesful"
]

StudentC = [
    "aray",
    "pithon",
    "recieve",
    "enviroment",
    "acommodate",
    "teh",
    "wierd"
]

students = ["StudentA", "StudentB", "StudentC"]
names = ["Kristof Michiels", "Stijn Doggen", "Vincent Nys"]

# Lege matrix maken
#zorg voor geen duplicates
mistakes = {
    student1: { student2: [] for student2 in students if student2 != student1}
    for student1 in students
}

identities: dict = {name: student for student, name in zip(students, names)}

folder = Path(input("Enter the path of the to be searched folder:\n>"))

pairings = [(students[i], students[(i + 1) % len(students)])for i in range(len(students))]

print(pairings)

for student_folderA in folder.iterdir():
    if student_folderA.is_dir():
        for fileA in student_folderA.iterdir():

            for student_folderB in folder.iterdir():
                if student_folderB == student_folderA:
                    continue
                elif student_folderB.is_dir():
                    for fileB in student_folderB.iterdir():
                        if fileA.read_text() == fileB.read_text():
                            if not student_folderA.name == student_folderB.name:
                                if (identities[student_folderA.name], identities[student_folderB.name]) in pairings:
                                    mistakes[identities[student_folderA.name]][identities[student_folderB.name]].append('zelfde bestand!')                        

print(mistakes)

env = jinja.Environment(
    loader=jinja.FileSystemLoader("./templates/"),
    autoescape=jinja.select_autoescape()
)

template = env.get_template("main.html")

print(template.render(
    authors=students,
    mistakes=mistakes
))