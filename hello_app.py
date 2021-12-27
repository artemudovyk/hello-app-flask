from flask import Flask, render_template, url_for, flash, redirect
from forms import GreetingForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '9d8842eb2549ae3d7556d4a6d6e9be8f'

# Database (DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Greeting(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), primary_key=True)

    def __repr__(self):
        return f"Greeting('self.name')"


@app.route('/', methods=['GET', 'POST'])
def home():
    form = GreetingForm()
    if form.validate_on_submit():
        flash(f'Hello {form.name.data}!', 'success')
        return redirect(url_for('greeting'))
    return render_template('home.html', form=form)


@app.route('/greeting')
def greeting():
    return render_template('greeting.html')


@app.route('/who-came-before-you')
def greetings_history():
    return render_template('who-came-before-you.html')


if __name__ == '__main__':
    app.run(debug=True)
