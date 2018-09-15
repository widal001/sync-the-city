from app import API, db
from app.models import *
from flask_restful import reqparse, abort, Resource
from flask import request

class OrganizationItem(Resource):
    def get(self, org_id):
        return {'Org_Id': 'org1'}

    def put(self, org_id):
        pass

    def delete(self, org_id):
        pass

class OrganizationList(Resource):
    def get(self):
        return [
        {'Org_Id': 'org1'},
        {'Org_Id': 'org2'}
        ]

    def post(self):

        if not request.json:
            abort(400)

        db.session.add_all([
        Organization(name=x['name'],ein=x['ein'])for x in request.json
        ])
        db.session.commit()
        return request.json, 201

    def delete(self):
        pass

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



API.add_resource(OrganizationList, '/api/v1/organizations')
API.add_resource(OrganizationItem, '/api/v1/organizations/<org_id>')
API.add_resource(ResourceList, '/api/v1/resources')
API.add_resource(ResourceItem, '/api/v1/resources/<resource_id>')
