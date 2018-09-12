from app import api, db
from app.models import *
from flask_restful import reqparse, abort, Resource

class OrganizationItem(Resource):
    def get(self, org_id):
        pass

    def put(self, org_id):
        pass

    def delete(self, org_id):
        pass

class OrganizationList(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

class ResourceItem(Resource):
    def get(self, resource_id):
        pass

    def put(self, resource_id):
        pass

    def delete(self, resource_id):
        pass

class ResourcenList(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass



api.add_resource(OrganizationList, '/api/v1/organizations')
api.add_resource(OrganizationItem, '/api/v1/organizations/<org_id>')
api.add_resource(ResourceList, '/api/v1/resources')
api.add_resource(ResourceItem, '/api/v1/resources/<resource_id>')
