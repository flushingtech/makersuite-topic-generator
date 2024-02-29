import pathlib
import textwrap


import inspect

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


API_KEY = ''


genai.configure(api_key=API_KEY)


# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
        

model = genai.GenerativeModel('gemini-pro')




base_query = 'You are an expert in running small 2-hour long hackathons. \
    Your responsibility is to take a broader topic and narrow it down in scope.\
        Provide a list of 3-5 subtopics that can be explored within two hours.\
            The broader topic we would like to explore is '
            
while True:
    topic = input('Provide a topic: ')
    query = base_query + topic
    
    response = model.generate_content(query)

    md = to_markdown(response.text)
    
    print(inspect.getmembers(md)[2][1]['data'].replace('   - ', '\n   - '))
    