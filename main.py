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
            <img class="logo"
                src="https://via.placeholder.com/100x40?text=Knowit Git" />
            Velkommen til Git kurs!!!!!
        </header>
        <br/>
    '''

def body():
    return '''
        <div class="body">
            Målet er at dere skal kunne bruke git i team

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur maximus orci ipsum, et dictum tortor tristique et. Quisque mattis, erat luctus consectetur commodo, risus turpis semper orci, id consectetur neque nibh eget nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla sed mattis nisl, vel interdum ante. Pellentesque ac bibendum orci. Nulla feugiat massa eu nulla venenatis, et suscipit augue bibendum. In pulvinar quam eget nibh finibus porttitor. Phasellus a nisl libero. Proin diam diam, interdum fringilla est ut, facilisis convallis urna. Vivamus tincidunt ultrices varius. Vivamus tempus non nisl non sodales. Donec porta lobortis est sit amet lacinia. Donec dapibus elit ut purus lacinia scelerisque.
            Etiam tincidunt, augue nec egestas pretium, mauris mi tristique tortor, eget commodo felis mauris eget purus. Praesent a magna non augue eleifend laoreet eu vel augue. Nunc ac mauris vel neque euismod eleifend interdum nec mi. Donec egestas mi id urna auctor egestas. Curabitur venenatis justo eros, et luctus lacus feugiat eget. Quisque eros orci, porttitor ac vulputate non, ultricies vel eros. Vestibulum eu ultricies erat. Fusce rutrum interdum odio, ut viverra ipsum ultrices vel. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut aliquam mi sit amet urna placerat pellentesque. Quisque et varius nisi, sit amet lacinia nisl. In convallis sapien vel mi aliquam, ut elementum lectus accumsan.
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


def my_new_awesome_feature():
    ...


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
