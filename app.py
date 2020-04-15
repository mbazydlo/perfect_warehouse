from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def warehouseMain():
    return render_template('warehouseMain.html')

@app.route('/warehouseEquipment.html')
def warehouseEquipment():
    return render_template('warehouseEquipment.html')

@app.route('/warehouseMainLocations.html')
def warehouseMainLocations():
    return render_template('warehouseMainLocations.html', location = 'coś')

@app.route('/warehouseOrders.html')
def warehouseOrders():
    return render_template('warehouseOrders.html')

@app.route('/warehouseProducts.html')
def warehouseProducts():
    return render_template('warehouseProducts.html')

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