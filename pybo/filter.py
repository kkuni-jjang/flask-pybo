def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)

import markdown
from markupsafe import Markup

def markdown_to_html(text):
    return Markup(markdown.markdown(text, extensions=['fenced_code', 'codehilite']))