from django.template import Context
from django.template.loader import get_template

from utils import get_definitions
from utils import get_indicators

definitions = [
    {'id': 1, 'name': "World Bank", 'definition': """Sustainable development recognizes that growth must be both inclusive and environmentally sound to reduce poverty and build shared prosperity for todays population and to continue to meet the needs of future generations. It is efficient with resources and carefully planned to deliver both immediate and long-term benefits for people   planet   and prosperity.
A sustainable path of development and poverty reduction would be one that (i) manages the resources of our planet for the future generation (ii) ensures social inclusion (iii) adopts fiscally responsible policies that limit future debt burden.""",
     'tbl_scope': 'Environmental,Social,Economic', 'domain': 'Generic', 'remarks': ''},

    {'id': 2, 'name': "State Bank", 'definition': """Sustainable development recognizes that growth must be both inclusive and environmentally sound to reduce poverty and build shared prosperity for todays population and to continue to meet the needs of future generations. It is efficient with resources and carefully planned to deliver both immediate and long-term benefits for people   planet   and prosperity.
    A sustainable path of development and poverty reduction would be one that (i) manages the resources of our planet for the future generation (ii) ensures social inclusion (iii) adopts fiscally responsible policies that limit future debt burden.""",
     'tbl_scope': 'Environmental,Economic', 'domain': 'Manufacturing', 'remarks': ''}
]

from forms import SystemBoundaryForm

def select_system_boundary(data):
    """
    Form the HTML context and then send it over as per sustainability definitions.

    :param data:
    :return:
    """
    system_boundary_form = SystemBoundaryForm()

    html_template = get_template("methods/system_boundary.html")
    context = Context({"system_boundary_form": system_boundary_form})
    system_boundary_form_html = html_template.render(context)
    return system_boundary_form_html

def generate_requirements(data):
    """
    Render HTML context as per generate requirements.
    :param data:
    :return:
    """

    html_template = get_template("methods/generate_requirements.html")
    context = Context({})
    generate_requirements_html = html_template.render(context)
    return generate_requirements_html


def select_sustainability_definitions(data):
    """
    Filter sustainability definitions based on tbl_scope and domain.
    :param data:
    :return:
    """

    problem_type = data.get('problem_type')
    domain = data.get('domain')
    tbl_scope = data.get('tbl_scope')

    definitions = get_definitions( domain, tbl_scope)


    html_template = get_template("methods/sustainability_definitions.html")

    names = [each.name for each in definitions]

    context = Context({"names": names})
    sustainability_definitions_html = html_template.render(context)
    return sustainability_definitions_html


    # Form the HTML context and then send it over as per sustainability definitions.
    # return definitions_dict

def select_sustainability_indicators(data):
    """

    :param data:
    :return:
    """
    print data


    tbl_scope = data.get('tbl_scope')

    indicators = get_indicators(tbl_scope)

    html_template = get_template("methods/sustainability_indicators.html")

    context = Context({"indicators": indicators})
    sustainability_indicators_html = html_template.render(context)
    return sustainability_indicators_html

def select_methods_tc(data):
    """

    :param data:
    :return:
    """
    html_template = get_template("methods/select_methods.html")

    names = [each.name for each in definitions]

    context = Context({"indicators": names})
    select_methods_tc = html_template.render(context)
    return select_methods_tc
