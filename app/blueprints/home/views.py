from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from app.forms import MainLocationForm, EquipmentForm, EquipmentCertification
from app import db
from app import models


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def warehouse_main():
    return render_template('warehouseMain.html')

@main.route('/warehouseEquipment')
def warehouse_equipment():
    all = models.WarehouseEquipment.query.order_by(models.WarehouseEquipment.equipment_name).all()
    return render_template('warehouseEquipment.html', all = all)


@main.route('/warehouseEquipmentAdd.html', methods=['GET', 'POST'])
def warehouse_equipment_add():
    form = EquipmentForm()
    main_locations = [(wml.id, wml.main_location_name) for wml in models.WarehouseMainLocation.query.all()]
    form.main_location_id.choices = main_locations

    if request.method == 'POST':
        new_equipment = models.WarehouseEquipment(
            form.equipment_name.data,
            form.main_location_id.data
        )
        db.session.add(new_equipment)
        db.session.commit()
        return redirect(url_for('main.warehouse_equipment'))

    return render_template('warehouseEquipmentAdd.html', form=form)


@main.route('/warehouseEquipmentEdit', methods=['GET', 'POST'])
def warehouse_equipment_edit():
    form = EquipmentForm()
    equipment_id = request.args.get('equipmentId')
    data = db.session.query(models.WarehouseEquipment).filter_by(id=equipment_id)
    main_locations = [(wml.id, wml.main_location_name) for wml in models.WarehouseMainLocation.query.all()]
    form.main_location_id.choices = main_locations
    if request.method == 'POST':
        data.update({"equipment_name" : form.equipment_name.data,
            "main_location_id" : form.main_location_id.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('main.warehouse_equipment'))
    return render_template('warehouseEquipmentEdit.html', to_edit=data.first(), form=form)

@main.route('/warehouseEquipmentDelete', methods=['GET', 'POST'])
def warehouse_equipment_delete():
    equipment_id = request.args.get('equipmentId')
    to_delete = db.session.query(models.WarehouseEquipment).filter_by(id=equipment_id)
    if request.method == 'POST':
        to_delete.delete()
        db.session.commit()
        return redirect(url_for('main.warehouse_equipment'))
    return render_template('warehouseEquipmentDelete.html', to_delete=to_delete.first())

@main.route('/warehouseEquipmentCertification', methods=['GET', 'POST'])
def warehouse_equipment_certification():
    equipment_id = request.args.get('equipmentId')
    form = EquipmentCertification()
    if request.method == 'POST':
        return redirect(url_for('main.warehouse_equipment'))
    all = db.session.query(models.WarehouseEquipmentCertification).filter_by(id=equipment_id).all()
    return render_template('warehouseEquipmentCertification.html', all = all, form=form)


@main.route('/warehouseMainLocations')
def warehouse_main_locations():
    all = models.WarehouseMainLocation.query.order_by(models.WarehouseMainLocation.main_location_name).all()
    return render_template('warehouseMainLocations.html', all = all)

@main.route('/warehouseMainLocationsAdd', methods=['GET', 'POST'])
def warehouse_main_locations_add():
    form = MainLocationForm()
    if request.method == 'POST':
        new_main_location = models.WarehouseMainLocation(form.main_location_name.data,
                                                        form.main_location_address.data)
        db.session.add(new_main_location)
        db.session.commit()
        return redirect(url_for('main.warehouse_main_locations'))

    return render_template('warehouseMainLocationsAdd.html', form=form)

@main.route('/warehouseMainLocationsEdit', methods=['GET', 'POST'])
def warehouse_main_locations_edit():

    form = MainLocationForm()
    main_location_id = request.args.get('mainLocationId')
    data = db.session.query(models.WarehouseMainLocation).filter_by(id=main_location_id)
    if request.method == 'POST':
        data.update({"main_location_name" : form.main_location_name.data,
            "main_location_address" : form.main_location_address.data}, synchronize_session=False)
        db.session.commit()
        return redirect(url_for('main.warehouse_main_locations'))
    return render_template('warehouseMainLocationsEdit.html', to_edit=data.first(), form=form)


@main.route('/warehouseMainLocationsDelete', methods=['GET', 'POST'])
def warehouse_main_locations_delete():
    main_location_id = request.args.get('mainLocationId')
    to_delete = db.session.query(models.WarehouseMainLocation).filter_by(id=main_location_id)
    if request.method == 'POST':
        to_delete.delete()
        db.session.commit()
        return redirect(url_for('main.warehouse_main_locations'))
    return render_template('warehouseMainLocationsDelete.html', to_delete=to_delete.first())

@main.route('/warehouseOrders')
def warehouse_orders():
    return render_template('warehouseOrders.html')

@main.route('/warehouseProducts')
def warehouse_products():
    all = models.Product.query.order_by(models.Product.product_name).all()
    return render_template('warehouseProducts.html', all = all)

@main.route('/warehouseQuarantine')
def warehouse_quarantine():
    return render_template('warehouseQuarantine.html')

# @manager.route('/warehouseStaff')
# def warehouse_staff():
#     all = models.Stuff.query.all()
#     return render_template('manager/warehouseStaff.html', all=all)

@main.route('/warehouseStock')
def warehouse_stock():
    return render_template('warehouseStock.html')

@main.route('/warehouseStockControl')
def warehouse_stock_control():
    return render_template('warehouseStockControl.html')

@main.route('/warehouseStockLocations')
def warehouse_stock_locations():
    return render_template('warehouseStockLocations.html')