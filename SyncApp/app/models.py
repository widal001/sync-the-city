from app import db
from datetime import datetime

class Organization(db.Model):
    __tablename__ = 'organization'
    org_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    ein = db.Column(db.String(60), index=True, unique=True)
    website = db.Column(db.String(180), index=True)

    profiles = db.relationship("Profile", back_populates="organization")

    def __repr__(self):
        return '<Organization {}>'.format(self.name, self.org_id)

class Profile(db.Model):
    __tablename__ = 'profile'
    profile_id = db.Column(db.Integer, primary_key=True)
    org_id = db.Column(db.Integer, db.ForeignKey('organization.org_id'))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    website = db.Column(db.String(180))
    primary = db.Column(db.Boolean, unique=False, default=False)

    organization = relationship("Organization", back_populates="profiles")

    def __repr__(self):
        return '<Profile {}>'.format(
        self.org_id, self.time_stamp
        )

class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, index=True)
    name = db.Column(db.String(80), index=True)

    def __repr__(self):
        return '<Tag {}>'.format(
        self.tag_id, self.type, self.name
        )

class Resource(db.Model):
    __tablename__ = 'resource'
    resource_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, index=True)
    name = db.Column(db.String(80), index=True)

    def __repr__(self):
        return '<Resource {}>'.format(
        self.resource_id, self.type, self.name
        )

class Question(db.Model):
    __tablename__ = 'question'
    inventory_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255))

    def __repr__(self):
        return  '<Question {}>'.format(
        self.inventory_id, self.question_text
        )
