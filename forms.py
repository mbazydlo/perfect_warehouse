from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class MainLocationForm(FlaskForm):
    main_location_name = StringField('Nazwa Magazynu', validators=[DataRequired()])
    main_location_address = StringField('Adres Magazynu')
    submit = SubmitField('Potwierdź')

class EquipmentForm(FlaskForm):
    equipment_name = StringField('Nazwa Sprzętu', validators=[DataRequired()])
    main_location_id = SelectField('Lokalizacja Sprzętu', choices=[(1,1),(2,2)])
    submit = SubmitField('Potwierdź')

class EquipmentCertification(FlaskForm):
    date = DateField('Data')
    submit = SubmitField('Potwierdź')