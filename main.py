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
        <header>
            Velkommen til Git kurs
        </header>
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
    return '''
        <footer>
            Laget av Andreas, Edvard, Patrick fra Knowit

             <a href="https://github.com/pmo022/git-kurs">Link til repo</a>
        </footer>
    '''


stylesheet = '''
    <style>
        header {
            font-size: 20px;
            border-bottom: 1px solid black;
            margin-bottom: 30px;
            padding-bottom: 10px;
        }

        footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid black;
        }
    </style>
'''
