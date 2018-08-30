from app import db
from datetime import datetime

class Organization(db.Model):
    __tablename__ = 'organization'
    org_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    ein = db.Column(db.String(60), index=True, unique=True)
    website = db.Column(db.String(180), index=True)

    def __repr__(self):
        return '<Organization {}>'.format(self.name, self.org_id)

class Profile(db.Model):
    __tablename__ = 'profile'
    profile_id = db.Column(db.Integer, primary_key=True)
    org_id = db.Column(db.Integer, db.ForeignKey('organization.org_id'))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    website = db.Column(db.String(180))
    primary = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        return '<Profile {}>'.format(
        self.org_id, self.time_stamp
        )
