lazy import jinja2 as jinja

env = jinja.Environment(
    loader = jinja.FileSystemLoader("./templates/"),
    autoescape = jinja.select_autoescape()
)

template = env.get_template("jinja01.html")

print(template.render(
    fruits = ["appel", "peer", "banaan"]
))