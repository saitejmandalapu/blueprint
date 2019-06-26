from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getfun',methods=['POST'])
def getfun():
	return '{"result" : "You are in Api Folder"}'