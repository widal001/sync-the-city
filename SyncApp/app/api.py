from app import API, db
from app.models import *
from flask_restful import abort, Resource, fields, marshal_with
from flask import request

class OrganizationItem(Resource):
    org_fields = {
        'name': fields.String,
        'ein': fields.String,
        'org_id': fields.Integer
    }

    @marshal_with(org_fields)
    def get(self, org_id):
        result = Organization.query.get(org_id)
        return result, 201

    @marshal_with(org_fields)
    def put(self, org_id):
        if not request.json:
            abort(400)
        org = Organization.query.get(org_id)
        for k,v in request.json.items():
            setattr(org, k, v)
        db.session.commit()
        result = Organization.query.get(org_id)
        return result, 201

    def delete(self, org_id):
        pass

class OrganizationList(Resource):
    org_fields = {
        'name': fields.String,
        'ein': fields.String,
        'org_id': fields.Integer
    }

    @marshal_with(org_fields)
    def get(self):
        result = db.session.query(Organization).all()
        return result, 201

    def post(self):
        if not request.json:
            abort(400)
        db.session.add_all([Organization(name=x['name'],ein=x['ein'])
                            for x in request.json])
        db.session.commit()
        return request.json, 201

    def delete(self):
        pass

class ProfileItem(Resource):

    profile_fields = {
        'profile_id': fields.String,
        'website': fields.String,
        'staff_size': fields.Integer,
        'budget': fields.Integer,
        'primary': fields.Integer
    }

    org_fields = {
        'org_id': fields.Integer,
        'name': fields.String(attribute='organization.name'),
        'ein': fields.String(attribute='organization.ein'),
        'profile': profile_fields
    }

    @marshal_with(org_fields)
    def get(self, org_id):
        result = (db.session.query(Profile)
                             .filter(Profile.org_id==org_id,
                                     Profile.primary==True)
                             .first())
        return result, 201

    def post(self, org_id):
        pass

class ProfileList(Resource):

    profile_fields = {
        'profile_id': fields.String,
        'website': fields.String,
        'staff_size': fields.Integer,
        'budget': fields.Integer,
        'primary': fields.Integer
    }

    org_fields = {
        'org_id': fields.Integer,
        'name': fields.String(attribute='organization.name'),
        'ein': fields.String(attribute='organization.ein'),
        'profile': profile_fields
    }

    @marshal_with(org_fields)
    def get(self):
        result = (db.session.query(Profile)
                             .filter(Profile.primary==True)
                             .all())

        return result, 201


class ResourceItem(Resource):
    def get(self, resource_id):
        pass

    def put(self, resource_id):
        pass

    def delete(self, resource_id):
        pass

class ResourceList(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

class OrgItemFull(Resource):

    profile_fields = {
        'profile_id': fields.String,
        'website': fields.String,
        'staff_size': fields.Integer,
        'budget': fields.Integer,
        'primary': fields.Integer
    }

    proposal_fields = {
        'prop_id': fields.Integer,
        'type': fields.String,
        'description': fields.String
    }

    org_fields = {
        'name': fields.String,
        'ein': fields.String,
        'org_id': fields.Integer,
        'profile': fields.Nested(profile_fields, attribute='current_profile'),
        'requests': fields.Nested(proposal_fields),
        'opportunities': fields.Nested(proposal_fields)
    }

    @marshal_with(org_fields)
    def get(self, org_id):
        result = Organization.query.get(org_id)
        return result, 201

    def post(self):
        pass

    def delete(self):
        pass


API.add_resource(OrganizationList, '/api/v1/organizations')
API.add_resource(OrganizationItem, '/api/v1/organizations/<org_id>')
API.add_resource(ProfileItem, '/api/v1/profiles/<org_id>')
API.add_resource(ResourceList, '/api/v1/resources')
API.add_resource(ResourceItem, '/api/v1/resources/<resource_id>')
API.add_resource(ProfileList, '/api/v1/profiles')
API.add_resource(OrgItemFull, '/api/v1/organizations-full/<org_id>')
