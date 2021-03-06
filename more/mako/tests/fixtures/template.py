import morepath
from more.mako import MakoApp


class App(MakoApp):
    pass


@App.path(path="persons/{name}")
class Person:
    def __init__(self, name):
        self.name = name


@App.template_directory()
def get_template_dir():
    return "templates"


@App.html(model=Person, template="person.mako")
def person_default(self, request):
    return {"name": self.name}


if __name__ == "__main__":
    morepath.run(App())
