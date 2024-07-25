from flask import Flask, render_template, request, redirect, url_for
from models import db, PatientRecord
from config import Config
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    records = PatientRecord.query.all()
    return render_template('index.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        medical_history = request.form['medical_history']

        new_record = PatientRecord(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            medical_history=medical_history
        )
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_record.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
