from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pat'}
    posts  = [
        {
            'author':{'username':'John'},
            'body':'Don\'t you just love coronavirus?'
        },
        {
            'author':{'username':'Pat'},
            'body':'This is my fucking blog.'
        },
        {
            'author':{'username':'Chuck'},
            'body':'Check out this microblog, pretty neat huh?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/insult')
def insult():
    user = {'username': 'Pat'}
    posts  = [
        {
            'author':{'username':'Computer'},
            'body':'You Fucking Suck!!'
        }
    ]
    return render_template('index.html', title='Insult', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
