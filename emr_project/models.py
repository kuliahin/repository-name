from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    medical_history = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<PatientRecord {self.first_name} {self.last_name}>'

db = SQLAlchemy()

class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    medical_history = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<PatientRecord {self.first_name} {self.last_name}>'
