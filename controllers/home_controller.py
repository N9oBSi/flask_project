from flask import render_template

def home_page():
    return render_template('home.html')

def events():
    events = [
        {'id': 1, 'text': "Doctor's appointment", 'date': '2024-04-30'},
        {'id': 2, 'text': "Team meeting at work", 'date': '2024-05-01'},
        {'id': 3, 'text': "Friend's wedding", 'date': '2024-05-15'}
    ]
    return render_template('events.html', events=events)

def privacy():
    data = {
        'children': ['Mitko', 'Ivancho', 'Gosho'],
        'tracking_technologies': ['Camera', 'GPS', 'Microphone']
    }
    return render_template('privacy.html', data=data)