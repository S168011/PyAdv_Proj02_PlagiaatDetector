lazy import jinja2 as jinja

env = jinja.Environment(
    loader = jinja.FileSystemLoader("./templates/"),
    autoescape = jinja.select_autoescape()
)

template = env.get_template("jinja02.html")

print(template.render(
    price_list = {"appel": 3, "peer": 1, "banaan": 2}
))