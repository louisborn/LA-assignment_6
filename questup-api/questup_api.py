from flask import Flask, request
from flask_cors import CORS

from mongodb_handler import MongoDBHandler

app = Flask(__name__)
CORS(app)

BASE_URL = '/quest-up/'
_db = MongoDBHandler()


@app.route(BASE_URL + '<teacher_id>/<subject_id>/quests')
def get_quests(teacher_id, subject_id):
    """
    Parameters
    ----------
    :param teacher_id: the unique teacher identifier
    :param subject_id: the unique subject identifier
    :return: the list of quests
    """
    return _db.get_quests(teacher_id, subject_id)


@app.route(BASE_URL + '<teacher_id>/annual-rewards')
def get_annual_rewards(teacher_id):
    """
    Parameters
    ----------
    :param teacher_id: the unique teacher identifier
    :return: the list of annual rewards
    """
    return _db.get_annual_rewards(teacher_id)


@app.route(BASE_URL + '<student_id>/quests/<quest_id>/submit', methods=['POST'])
def submit_student_quest_result(student_id, quest_id):
    """
    Parameters
    ----------
    :param student_id: the unique student identifier
    :param quest_id: the unique quest identifier
    :return:
    """
    json_data = request.get_json()  # Get the quest data object
    quest = json_data.get("quest")
    pass


@app.route(BASE_URL + 'students/<student_id>')
def get_student(student_id):
    """
    Parameters
    ----------
    :param student_id: the unique student identifier
    :return: the student data object
    """
    return _db.get_student(student_id)


@app.route(BASE_URL + 'shop-items/<teacher_id>')
def get_shop_items(teacher_id):
    """
    Parameters
    ----------
    :param teacher_id: the unique teacher identifier
    :return: the list of available shop items
    """
    return _db.get_shop_items(teacher_id)


app.run(host="0.0.0.0", port=6001)