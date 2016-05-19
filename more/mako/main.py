import morepath
from mako.lookup import TemplateLookup


class MakoApp(morepath.App):
    pass


@MakoApp.setting_section(section='mako')
def get_setting_section():
    return {
        'default_filters': ['h'],
        'format_exceptions': False,
        'input_encoding': 'utf-8',
        'output_encoding': 'utf-8',
        'strict_undefined': False
        }


@MakoApp.template_loader(extension='.mako')
def get_mako_loader(template_directories, settings):
    config = settings.mako.__dict__.copy()
    config.update({
        'directories': template_directories
        })
    return TemplateLookup(**config)


@MakoApp.template_render(extension='.mako')
def get_mako_render(loader, name, original_render):
    template = loader.get_template(name)

    def render(content, request):
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
