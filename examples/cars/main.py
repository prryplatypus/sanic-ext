from sanic import Sanic
from sanic_ext import oa3bp

from blueprints.car import blueprint as car_blueprint
from blueprints.driver import blueprint as driver_blueprint
from blueprints.garage import blueprint as garage_blueprint
from blueprints.manufacturer import blueprint as manufacturer_blueprint
from blueprints.repair import blueprint as repair_blueprint

app = Sanic("Cars API example")

app.blueprint(car_blueprint)
# app.blueprint(driver_blueprint)
# app.blueprint(garage_blueprint)
# app.blueprint(manufacturer_blueprint)
# app.blueprint(repair_blueprint)

app.blueprint(oa3bp)

app.config.API_VERSION = "1.0.0"
app.config.API_TITLE = "Car API"
app.config.API_TERMS_OF_SERVICE = "http://example.org/TOS"
app.config.API_CONTACT_EMAIL = "channelcat@gmail.com"
app.config.API_DESCRIPTION = "Cars API example"

app.run(port=8001, debug=True)