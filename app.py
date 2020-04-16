from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import model

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'taki sobie sekret'

db = SQLAlchemy(app)

class MainLocation(FlaskForm):
    main_location_name = StringField('Nazwa Magazynu', validators=[DataRequired()])
    main_location_address = StringField('Adres Magazynu')
    submit = SubmitField('Potwierdź')

@app.route('/')
def warehouseMain():
    return render_template('warehouseMain.html')

@app.route('/warehouseEquipment.html')
def warehouseEquipment():
    return render_template('warehouseEquipment.html')

@app.route('/warehouseMainLocations.html', methods=['GET', 'POST'])
def warehouseMainLocations():
    if request.method == 'POST':
        return redirect(url_for('warehouseMainLocationsAdd'))
    all = model.WarehouseMainLocation.query.order_by(model.WarehouseMainLocation.main_location_name).all()
    return render_template('warehouseMainLocations.html', all = all)

@app.route('/warehouseMainLocationsAdd.html', methods=['GET', 'POST'])
def warehouseMainLocationsAdd():
    form = MainLocation()
    if request.method == 'POST':
        new_main_location = model.WarehouseMainLocation(form.main_location_name.data,
                                                        form.main_location_address.data)
        db.session.add(new_main_location)
        db.session.commit()
        return redirect(url_for('warehouseMainLocations'))

    return render_template('warehouseMainLocationsAdd.html', form=form)

@app.route('/warehouseMainLocationsEdit.html', methods=['GET', 'POST'])
def warehouseMainLocationsEdit():

    form = MainLocation()
    main_location_id = request.args.get('mainLocationId')
    data = db.session.query(model.WarehouseMainLocation).filter_by(id=main_location_id)
    if request.method == 'POST':
        data.update({"main_location_name" : form.main_location_name.data,
            "main_location_address" : form.main_location_address.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('warehouseMainLocations'))
    return render_template('warehouseMainLocationsEdit.html', to_edit=data.first(), form=form)


@app.route('/warehouseMainLocationsDelete.html', methods=['GET', 'POST'])
def warehouseMainLocationsDelete():
    main_location_id = request.args.get('mainLocationId')
    to_delete = db.session.query(model.WarehouseMainLocation).filter_by(id=main_location_id)
    if request.method == 'POST':
        to_delete.delete()
        db.session.commit()
        return redirect(url_for('warehouseMainLocations'))
    return render_template('warehouseMainLocationsDelete.html', to_delete=to_delete.first())

@app.route('/warehouseOrders.html')
def warehouseOrders():
    return render_template('warehouseOrders.html')

@app.route('/warehouseProducts.html')
def warehouseProducts():
    return render_template('warehouseProducts.html')

@app.route('/warehouseQuarantine.html')
def warehouseQuarantine():
    return render_template('warehouseQuarantine.html')

@app.route('/warehouseStaff.html')
def warehouseStaff():
    return render_template('warehouseStaff.html')

@app.route('/warehouseStock.html')
def warehouseStock():
    return render_template('warehouseStock.html')

@app.route('/warehouseStockControl.html')
def warehouseStockControl():
    return render_template('warehouseStockControl.html')

@app.route('/warehouseStockLocations.html')
def warehouseStockLocations():
    return render_template('warehouseStockLocations.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)