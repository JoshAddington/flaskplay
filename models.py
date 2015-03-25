from app import db

class Station(db.Model):
        __tablename__ = "stations"

        pk=db.Column(db.Integer, primary_key=True)
        id=db.Column(db.Integer, unique=True)
        name=db.Column(db.String(128), unique=True)
        latitude=db.Column(db.Float)
        longitude=db.Column(db.Float)
        bikes = db.relationship('Bike', backref='bike', lazy='dynamic')


        def __init__(self, id, name, latitude, longitude):
                self.id = id
                self.name = name
                self.latitude = latitude
                self.longitude = longitude

        def __repr__(self):
                return '<id {}>'.format(self.id)

class Bike(db.Model):
        __tablename__ = "bikes"

        id=db.Column(db.Integer, primary_key=True)
        station_id=db.Column(db.Integer, db.ForeignKey('stations.id'))
        number_of_bikes=db.Column(db.Integer)
        time=db.Column(db.Time)
        date = db.Column(db.Date)

        def __init__(self, station_id, number_of_bikes, time, date):
                self.station_id = station_id
                self.number_of_bikes = number_of_bikes
                self.time = time
                self.date = date

        def __repr__(self):
                return '<id {}>'.format(self.id)
