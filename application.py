from flask import Flask,render_template,request, redirect, url_for
from pprint import PrettyPrinter
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

pp = PrettyPrinter(indent=4)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	phone = db.Column(db.String(80))
	twitter = db.Column(db.String(140))
	tags = db.relationship('Tag')
	payment_detail_id = db.relationship('PaymentDetail')


class PaymentDetail(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, ForeignKey=('user.id'))
	cardno = db.Column(db.String(20))
	start_date = db.Column(db.String(4))
	end_date = db.Column(db.String(4))
	
class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, ForeignKey('user.id')))
	tagid = db.Column(db.String(80), unique=True)
	balance = db.Column(db.Numeric(12,2))
	last_updated = db.Column(db.DateTime())

	def __init__(self, tagid, balance):
        self.tagid = tagid
        self.balance = balance

    def __repr__(self):
        return '<Tag %r>' % self.tagid


class History(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tagid =  db.Column(db.String(80), unique=False)
	old_balance = db.Column(db.Numeric(12,2))
	delta = db.Column(db.Numeric(12,2))
	new_balance = db.Column(db.Numeric(12,2))
	vendor_id = db.Column(db.Integer)

class Vendor(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))





@app.route("/", methods=['GET', 'POST', 'PUT'])
def slash():
	pass

@app.route("/associate/<tagid>/<cardno>")
def associate(tagid,cardno):
	pass

@app.route("/update/<tagid>/<balance>")
def update(tagid,balance):
	pass

@app.route("/balance/<tagid>")
def balance(tagid):
	pass



if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
