from flask_restx import Resource, Namespace
from flask import request
from services.auth import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/')
class AuthsView(Resource):
	def post(self):
		data = request.json

		username = data.get("username", None)
		password = data.get("password", None)

		if None in [username, password]:
			return "", 400

		tokens = auth_service.generate_tokens(username, password)

		return tokens, 201

	def put(self):
		data = request.json
		token = data.get("refresh_token")

		tokens = auth_service_refresh_token(token)

		return tokens, 201

@user_ns.route("/<int:uid>")
class UserView(Resource):
	@admin_required
	def delete(self, uid):
		user_service.delete(uid)

		return "", 204
