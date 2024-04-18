from flask_restx import Resource, Namespace
from flask import request
from container import user_service
from dao.model.user import UserSchema
from helpers.decorators import admin_required

user_ns = Namespace('users')

@user_ns.route('/')
class UsersView(Resource):
	def get(self):
		users = user_service.get_all()
		response = UserSchema(many=True).dump(users)

		return response, 200

	def post(self):
		data = request.json
		user = user_service.create(data)

		return "", 201, {"location": f"/users/{user.id}"}

@user_ns.route("/<int:uid>")
class UsersView(Resource):
	@admin_required
	def delete(self, uid):
		user_service.delete(uid)

		return "", 204
