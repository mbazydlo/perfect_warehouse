import os
import tempfile

import pytest

from app import create_app, db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app('test')

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_main_path(client):
    """Check does root url response"""

    response = client.get('/')
    assert response.status_code == 200

def test_products(client):
    """Check does root url response"""

    response = client.get('/warehouseProducts')
    assert response.status_code == 200

def test_main_locations(client):
    """Check does root url response"""

    response = client.get('/warehouseMainLocations')
    assert response.status_code == 200

def test_stock_locations(client):
    """Check does root url response"""

    response = client.get('/warehouseStockLocations')
    assert response.status_code == 200

def test_stock_locations(client):
    """Check does root url response"""

    response = client.get('/warehouseStockLocations')
    assert response.status_code == 200

def test_orders(client):
    """Check does root url response"""

    response = client.get('/warehouseOrders')
    assert response.status_code == 200

def test_quarantine(client):
    """Check does root url response"""

    response = client.get('/warehouseQuarantine')
    assert response.status_code == 200

def test_stock_control(client):
    """Check does root url response"""

    response = client.get('/warehouseStockControl')
    assert response.status_code == 200

def test_equipment(client):
    """Check does root url response"""

    response = client.get('/warehouseEquipment')
    assert response.status_code == 200