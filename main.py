from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    webpage = \
        stylesheet + \
        header() + \
        body() + \
        footer() 
    return webpage


def header():
    return f'''
        <div class="header">
            Velkommen til Git kurs
        </div>
        <br/>
    '''

def body():
    return '''
        <div class="body">
            Målet er at dere skal kunne bruke git i team
        </div>
        <br/>
    '''

def footer():
    return "Footer (todo lag footer her)"


stylesheet = '''
    <style>
        .header {
            font-size: 20px;
            border-bottom: 1px solid black; 
            margin-bottom: 28px;
            padding-bottom: 10px;
        }
    </style>
'''