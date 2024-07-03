from flask import Flask

app = Flask(__name__)
import controllers.auth, controllers.reg, controllers.main_page, controllers.profile, controllers.chat, controllers.game
app.secret_key = '&l(c(q62sh6es+8jkuhpl-hro-!9y_fhhdtrsl%7bp1*%k!rb9'
app.debug = True
