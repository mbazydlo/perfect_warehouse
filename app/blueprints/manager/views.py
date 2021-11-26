from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from forms import MainLocationForm, EquipmentForm, EquipmentCertification
from time import time
import app.models as models


manager = Blueprint('manager', __name__, template_folder='templates')


@manager.route('/warehouseStaff')
def warehouse_staff():
    all = models.Stuff.query.all()
    return render_template('manager/warehouseStaff.html', all=all)
