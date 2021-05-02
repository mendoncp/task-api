from flask import jsonify, request
from . import tasks

@tasks.route('/')
def list():
    return 'Get All Tasks'