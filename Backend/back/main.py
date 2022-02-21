from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
import usertoken


#tz1Td6zHZHrMRGvaZNTvBDsKrnGA2GrG647m

app = Flask(__name__)
api = Api(app)
cors = CORS(app,  )

token = usertoken.Token("tz1Td6zHZHrMRGvaZNTvBDsKrnGA2GrG647m")

user = {
    "user":{
            'token': token.get_account(),
            'balance': token.get_balance_account()
    }
    }

class Users(Resource):
    def get(self):
        return user

    def post(self):
        pass


api.add_resource(Users, '/')

if __name__ == '__main__':
    app.run(debug=True)