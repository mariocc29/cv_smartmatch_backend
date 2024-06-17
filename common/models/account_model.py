import mongoengine
from bcrypt import hashpw, gensalt
from rest_framework_simplejwt.tokens import AccessToken

class AccountModel(mongoengine.Document):
	meta = { 'collection': 'accounts' }

	email = mongoengine.EmailField(unique=True)
	password_digest = mongoengine.StringField()

	def set_password(self, password):
		hashed_password = hashpw(password.encode('utf-8'), gensalt())
		self.password_digest = hashed_password.decode('utf-8')
	
	def check_password(self, password):
		hashed_password = hashpw(password.encode('utf-8'), self.password_digest.encode('utf-8'))
		return hashed_password == self.password_digest.encode('utf-8')
	
	def is_authenticated(self, request=None):
		if request and 'Authorization' in request.headers:
			token = request.headers['Authorization'].split()[1]
			try:
				AccessToken(token)
				return True
			except:
				return False
		return False
