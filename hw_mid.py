from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    members = [{
        'username': '梁思婕',
        'age': 27,
        'birth': '04.23',
        'interest': 'Take beautiful pictures & 算命~'
    },
    {
        'username': '俞子悠',
        'age': 26,
        'birth': '03.23',
        'interest': 'Yoga & 打手遊 ~'
    },
    {
        'username': '李家名',
        'age': 35,
        'birth': '04.22',
        'interest': '寫作業~'
    },
    {
        'username': '陳昱辰',
        'age': 30,
        'birth': '04.22',
        'interest': '貸款~'
    },
    {
        'username': '陳昱齊',
        'age': 26,
        'birth': '07.20',
        'interest': 'EFK and Work~'
    }
    ]
    return render_template('info.html', members = members)

@app.route('/photo')
def photo():
    photos = [
        {
            'username': '梁思婕',
            'filename': 'images/lala.png'
        },
        {
            'username': '余子悠',
            'filename': 'images/yoyo.png'
        },
        {
            'username': '李家名',
            'filename': 'images/ming.png'
        },
        {
            'username': '陳昱辰',
            'filename': 'images/辰.png'
        },
        {
            'username': '陳昱齊',
            'filename': 'images/77_2.png'
        }
    ]
    return render_template('photo.html', photos = photos)

if __name__ == '__main__':
    app.run(debug=True)