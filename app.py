from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from forms import MainLocationForm, EquipmentForm, EquipmentCertification
from time import time
import model

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'taki sobie sekret'

db = SQLAlchemy(app)

@app.route('/')
def warehouseMain():
    return render_template('warehouseMain.html')

@app.route('/warehouseEquipment.html', methods=['GET', 'POST'])
def warehouseEquipment():
    if request.method == 'POST':
        return redirect(url_for('warehouseEquipmentAdd'))
    all = model.WarehouseEquipment.query.order_by(model.WarehouseEquipment.equipment_name).all()
    return render_template('warehouseEquipment.html', all = all)


@app.route('/warehouseEquipmentAdd.html', methods=['GET', 'POST'])
def warehouseEquipmentAdd():
    form = EquipmentForm()
    main_locations = [(wml.id, wml.main_location_name) for wml in model.WarehouseMainLocation.query.all()]
    form.main_location_id.choices = main_locations
    if request.method == 'POST':
        new_equipment = model.WarehouseEquipment(form.equipment_name.data,
                                                form.main_location_id.data)
        db.session.add(new_equipment)
        db.session.commit()
        return redirect(url_for('warehouseEquipment'))

    return render_template('warehouseEquipmentAdd.html', form=form)


@app.route('/warehouseEquipmentEdit.html', methods=['GET', 'POST'])
def warehouseEquipmentEdit():
    form = EquipmentForm()
    equipment_id = request.args.get('equipmentId')
    data = db.session.query(model.WarehouseEquipment).filter_by(id=equipment_id)
    main_locations = [(wml.id, wml.main_location_name) for wml in model.WarehouseMainLocation.query.all()]
    form.main_location_id.choices = main_locations
    if request.method == 'POST':
        data.update({"equipment_name" : form.equipment_name.data,
            "main_location_id" : form.main_location_id.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('warehouseEquipment'))
    return render_template('warehouseEquipmentEdit.html', to_edit=data.first(), form=form)

@app.route('/warehouseEquipmentDelete.html', methods=['GET', 'POST'])
def warehouseEquipmentDelete():
    equipment_id = request.args.get('equipmentId')
    to_delete = db.session.query(model.WarehouseEquipment).filter_by(id=equipment_id)
    if request.method == 'POST':
        to_delete.delete()
        db.session.commit()
        return redirect(url_for('warehouseEquipment'))
    return render_template('warehouseEquipmentDelete.html', to_delete=to_delete.first())

@app.route('/warehouseEquipmentCertification.html', methods=['GET', 'POST'])
def warehouseEquipmentCertification():
    equipment_id = request.args.get('equipmentId')
    form = EquipmentCertification()
    if request.method == 'POST':
        return redirect(url_for('warehouseEquipment'))
    all = db.session.query(model.WarehouseEquipmentCertification).filter_by(id=equipment_id).all()
    return render_template('warehouseEquipmentCertification.html', all = all, form=form)


@app.route('/warehouseMainLocations.html', methods=['GET', 'POST'])
def warehouseMainLocations():
    if request.method == 'POST':
        return redirect(url_for('warehouseMainLocationsAdd'))
    all = model.WarehouseMainLocation.query.order_by(model.WarehouseMainLocation.main_location_name).all()
    return render_template('warehouseMainLocations.html', all = all)

@app.route('/warehouseMainLocationsAdd.html', methods=['GET', 'POST'])
def warehouseMainLocationsAdd():
    form = MainLocationForm()
    if request.method == 'POST':
        new_main_location = model.WarehouseMainLocation(form.main_location_name.data,
                                                        form.main_location_address.data)
        db.session.add(new_main_location)
        db.session.commit()
        return redirect(url_for('warehouseMainLocations'))

    return render_template('warehouseMainLocationsAdd.html', form=form)

@app.route('/warehouseMainLocationsEdit.html', methods=['GET', 'POST'])
def warehouseMainLocationsEdit():

    form = MainLocationForm()
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
    app.run(port=5001, debug=True)