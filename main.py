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
            <img class="logo" 
                src="https://via.placeholder.com/100x40?text=Knowit Git" />
            Velkommen til Git kurs!
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
        </footer>
    '''


stylesheet = '''
    <style>
        header {
            font-size: 20px;
            border-bottom: 1px solid black; 
            margin-bottom: 30px;
            padding-bottom: 10px;
            display: flex;
            align-items: center;
        }
        header img {
            margin-right: 10px;
        }

        footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid black;
        }
    </style>
'''