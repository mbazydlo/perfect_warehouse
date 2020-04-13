from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def warehouseMain():
    return render_template('warehouseMain.html', message = 'To je Main')


if __name__ == '__main__':
    app.run(port=5000, debug=True)