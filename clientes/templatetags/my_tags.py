from django import template
import datetime

register = template.Library()

#takes_context permite acessar o contexo do template
@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def footer_message():
    return 'Desenvolvimento web com Django 2.0'
