from flask_sqlalchemy import SQLAlchemy
from app import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    product_description = db.Column(db.String, nullable=True)
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))

    productOnStock = db.relationship('ProductOnStock', backref='products', lazy = 'dynamic')
    order = db.relationship('Order', backref='product', lazy = 'dynamic')


class ProductOnStock(db.Model):
    __tablename__ = 'product_on_stock'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    qty = db.Column(db.Integer, default=0)
    main_location_id = db.Column(db.Integer, db.ForeignKey('warehouse_main_location.id'))
    stock_location_id = db.Column(db.Integer, db.ForeignKey('warehouse_stock_location.id'))
    quarantine_id = db.Column(db.Integer, db.ForeignKey('warehouse_quarantine.id'))


class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)
    product_category_name = db.Column(db.String)
    product_category_description = db.Column(db.String, nullable=True)




class WarehouseMainLocation(db.Model):
    __tablename__ = 'warehouse_main_location'
    id = db.Column(db.Integer, primary_key=True)
    main_location_name = db.Column(db.String)
    main_location_address = db.Column(db.String, nullable=True)

    productOnStock = db.relationship('ProductOnStock', backref='warehouse_main_location', lazy = 'dynamic')
    warehouseEquipment = db.relationship('WarehouseEquipment', backref='warehouse_main_location', lazy = 'dynamic')
    warehouseStockLocation = db.relationship('WarehouseStockLocation', 
                                             backref='warehouse_main_location', 
                                             lazy = 'dynamic')
    
                                             

class WarehouseStockLocation(db.Model):
    __tablename__ = 'warehouse_stock_location'
    id = db.Column(db.Integer, primary_key=True)
    stock_location_name = db.Column(db.String)
    main_location_id = db.Column(db.Integer, db.ForeignKey('warehouse_main_location.id'))

    productOnStock = db.relationship('ProductOnStock', backref='warehouse_stock_location', lazy = 'dynamic')

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    customer_id = db.Column(db.Integer)
    completing_by = db.Column(db.Integer, db.ForeignKey('stuff.id'))
    is_on_hold = db.Column(db.Boolean, default=False)

class WarehouseQuarantine(db.Model):
    __tablename__ = 'warehouse_quarantine'
    id = db.Column(db.Integer, primary_key=True)
    quarantine_details = db.Column(db.String)

    productOnStock = db.relationship('ProductOnStock', backref='warehouse_quarantine', lazy = 'dynamic')

class WarehouseEquipment(db.Model):
    __tablename__ = 'warehouse_equipment'
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String)
    main_location_id = db.Column(db.Integer, db.ForeignKey('warehouse_main_location.id'))
    warehouseEquipmentCertification = db.relationship('WarehouseEquipmentCertification',
                                                        backref='stuff',
                                                        lazy = 'dynamic')

class Stuff(db.Model):
    __tablename__ = 'stuff'
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    hire_date = db.Column(db.Date)
    end_date = db.Column(db.Date, nullable=True)

    order = db.relationship('Order', backref='stuff', lazy = 'dynamic')


class WarehouseEquipmentCertification(db.Model):
    __tablename__ = 'warehouse_equipment_certification'
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('warehouse_equipment.id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date, nullable=True)