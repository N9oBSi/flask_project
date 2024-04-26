from flask import render_template

def home_page():
    return render_template('home.html')


def privacy():
    data = {
        'children': ['Mitko', 'Ivancho', 'Gosho'],
        'tracking_technologies': ['Camera', 'GPS', 'Microphone']
    }
    return render_template('privacy.html', data=data)