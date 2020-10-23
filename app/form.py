from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Form(FlaskForm):

    min = IntegerField("minutes", render_kw={"placeholder": "gonna wait a while..."})
    sec = IntegerField("seconds", render_kw={"placeholder": "lets just do seconds"})
    ms = IntegerField("ms")
    submit = SubmitField("START!")
