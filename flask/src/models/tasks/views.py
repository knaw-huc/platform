from flask import Blueprint, render_template, request, session, url_for, flash, jsonify
from src.common.back import back
import src.models.users.decorators as user_decorators
from .tracked_task import TrackedTask

__author__ = 'tom'

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/')
@user_decorators.requires_login
@back.anchor
def user_tasks():
    return jsonify(TrackedTask.get_all_by_user_email(session['email']))