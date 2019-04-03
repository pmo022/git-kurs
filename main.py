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
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur maximus orci ipsum, et dictum tortor tristique et. Quisque mattis, erat luctus consectetur commodo, risus turpis semper orci, id consectetur neque nibh eget nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla sed mattis nisl, vel interdum ante. Pellentesque ac bibendum orci. Nulla feugiat massa eu nulla venenatis, et suscipit augue bibendum. In pulvinar quam eget nibh finibus porttitor. Phasellus a nisl libero. Proin diam diam, interdum fringilla est ut, facilisis convallis urna. Vivamus tincidunt ultrices varius. Vivamus tempus non nisl non sodales. Donec porta lobortis est sit amet lacinia. Donec dapibus elit ut purus lacinia scelerisque.
            Etiam tincidunt, augue nec egestas pretium, mauris mi tristique tortor, eget commodo felis mauris eget purus. Praesent a magna non augue eleifend laoreet eu vel augue. Nunc ac mauris vel neque euismod eleifend interdum nec mi. Donec egestas mi id urna auctor egestas. Curabitur venenatis justo eros, et luctus lacus feugiat eget. Quisque eros orci, porttitor ac vulputate non, ultricies vel eros. Vestibulum eu ultricies erat. Fusce rutrum interdum odio, ut viverra ipsum ultrices vel. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut aliquam mi sit amet urna placerat pellentesque. Quisque et varius nisi, sit amet lacinia nisl. In convallis sapien vel mi aliquam, ut elementum lectus accumsan.
            Vivamus cursus lacinia magna non tristique. Fusce commodo odio quis pulvinar tincidunt. Etiam rutrum semper tempus. Mauris malesuada porttitor urna, eleifend suscipit sapien sollicitudin id. Sed in lectus elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada tellus sapien, vitae consectetur libero volutpat ac. Ut aliquet eros ut dui gravida, nec scelerisque nunc condimentum. Pellentesque et elementum quam. Quisque posuere nisi ac lorem consectetur, sed faucibus massa vulputate. Etiam finibus metus ac justo ultrices ultricies. Fusce ullamcorper erat tellus, ut mattis quam pulvinar nec.
            Aliquam porttitor mi ligula, nec elementum eros lacinia nec. In in urna eu lectus laoreet rutrum cursus in metus. Praesent maximus velit vitae nisi dignissim consequat. Proin augue lacus, porta id laoreet eget, suscipit ut neque. Nulla dignissim, dolor ac tincidunt auctor, velit eros commodo felis, vitae vulputate mi erat eget nibh. Aenean dignissim sed sem vel vehicula. Suspendisse tristique aliquam faucibus. Aenean viverra elit sit amet condimentum pellentesque. Vivamus eget augue tellus. Pellentesque posuere quis nulla ut tincidunt. Sed sit amet porta ligula. Vivamus accumsan neque nisi, sed blandit felis pharetra eu. Cras a commodo dolor. Mauris pulvinar nisi vestibulum, convallis lacus eget, viverra sem. Ut convallis convallis sapien in elementum. Sed vestibulum, est quis dignissim sollicitudin, dolor augue maximus nisl, quis sodales odio velit vel ex.
            Sed ornare pellentesque est, quis gravida sem aliquet vel. Donec vestibulum volutpat posuere. Fusce interdum pulvinar fringilla. Phasellus ultrices pulvinar gravida. Vivamus lacinia dapibus velit, nec dignissim magna fringilla at. Praesent sollicitudin efficitur ante, ac placerat odio ornare at. Duis in nibh nec libero vestibulum commodo nec eget erat. Integer interdum tortor vel egestas laoreet. Ut placerat imperdiet risus, consectetur vehicula nisi vestibulum non.
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
        }

        footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid black;
        }
    </style>
'''