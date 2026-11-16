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
names = ["Kristof", "Stijn", "Isaac"]

# Lege matrix maken
mistakes = {
    student1: {
        student2: []
        for student2 in students
        if students.index(student2) > students.index(student1)
    }
    for student1 in students
}

# Manueel opmerkingen toevoegen
mistakes["StudentA"]["StudentB"].append('zelfde spelfout: "aray"')
mistakes["StudentA"]["StudentB"].append('zelfde spelfout: "pithon"')

mistakes["StudentA"]["StudentC"].append('zelfde spelfout: "aray"')
mistakes["StudentA"]["StudentC"].append('zelfde spelfout: "pithon"')

mistakes["StudentB"]["StudentC"].append('zelfde spelfout: "aray"')
mistakes["StudentB"]["StudentC"].append('zelfde spelfout: "pithon"')

#StudentA: Kristof, StudentB: ... laten genereren. keys met f-string?
identities: dict = {student: name for student, name in zip(students, names)}

env = jinja.Environment(
    loader=jinja.FileSystemLoader("./templates/"),
    autoescape=jinja.select_autoescape()
)

template = env.get_template("main.html")

print(template.render(
    authors=students,
    mistakes=mistakes
))