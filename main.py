from flask import Flask
from flask import render_template, redirect, url_for
from datetime import datetime, timedelta
from flask import request
from plyer import notification
import base64

app = Flask(__name__)

items = {}

@app.route('/')
def index():
    pushNotification()
    return render_template('index.html',
                            items=items.values())


@app.route('/create')
def create():
    time = str(datetime.now())[0:10].split('-')
    time = time[2] + '/' + time[1] + '/' + time[0]
    return  render_template('create.html',
                           time=time,
                           items=items.values())

@app.route('/new/<id>/')
def show_item(id):
    time = str(datetime.now())[0:10].split('-')
    time = time[2] + '/' + time[1] + '/' + time[0]
    new_item = items[int(id)]
    return render_template('new_item.html',
                           id=new_item['id'],
                           name=new_item['name'],
                           date=new_item['date'],
                           image=new_item['image'],
                           time=time,
                           )


def new_items(name, date, image):
    new_id = len(items.keys()) + 1
    return {
        'id': new_id,
        'name': name,
        'date': date,
        'image': image
    }


@app.route('/new/create/', methods=['POST'])
def create_new_item():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        image = request.files['image']
        
        image_str = base64.b64encode(image.read())
        image_str = image_str.decode('utf-8')
        image = image_str

        item = new_items(name, date, image)
        # print(item)
        items[item['id']] = item
        return redirect(url_for('index'))
    
@app.route('/delete/',methods=['POST'])
def delete():
    x = int(request.form['title'])
    del[items[x]]
    return redirect(url_for('index'))

# @app.route('/new/create/', methods=['POST'])
# def create_new_item():
#     item = new_items(request.form['name'],
#                      request.form['date'],
#                      request.files['image'])
#     items[item['id']] = item
#     return redirect(url_for('index'))

def pushNotification():
    # time format(yyyy/mm/dd), date format(dd/mm/yyyy)
    time = [int(i) for i in str(datetime.now())[0:10].split('-')]
    d31  = [1,3,5,7,8,10,12]
    
    selected = ''
    count = 0
    for item_ID in items.values():
        date = [int(i) for i in item_ID['date'].split('/')]    
        if date[2] == time[0]:
            left = 999999
            if time[1] - date[1] == 1:

                day = 30
                if time[1] in d31:
                    day = 31
                elif time[1] == 2:
                    if time[0]%4 == 0: 
                        day = 29
                    else: 
                        day = 28

                left = day-time[2] + date[0]
            
            elif time[1] == date[1]:
                left = date[0] - time[2]
            
            if left <= 7:
                count += 1
                selected = f'{item_ID["name"]} will in expired on {item_ID["date"]} ({left} day(s)).\n'
                notification.notify(
        title="BeforeEXP", 
        message= selected,
        timeout=20 )
    
    # if count > 0:
    #     tell = f'You have {count} item(s) will be expired soon!\n' + selected
    #     notification.notify(
    #     title="BeforeEXP", 
    #     message= tell,
    #     timeout=20 )