from flask import Flask, redirect, request, render_template
import threading
import random
from app.form import Form
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


class Timer:
    def __init__(self):
        self.min = 0
        self.sec = 0
        self.ms = 0

    def time(self):
        def mytimer():
            my_timer = threading.Timer(.01, mytimer)
            my_timer.start()
            self.time_check()
            if  self.min == 0 and self.sec == 0 and self.ms == 1:
                my_timer.cancel()
                self.winner()
        mytimer()

    def time_check(self):
        if self.ms == 0:
            self.ms = 100
            self.sec -= 1
        if self.sec == 0 and self.min != 0: 
            self.sec = 60
            if self.min != 0:
                self.min -= 1
        self.ms -= 1
        # print(self.min)
        # print(self.sec)
        # print(self.ms)
    
    def __repr__(self):
        return f'{self.min}:{self.sec}:{self.ms}'

    def winner(self):
            return random.choice(["Geoffrey", "Mylo", "Julie", "Kasey", "Jeff", "James", "Alec", "Ivan"])

    def reset(self):
        self.sec = 5

    def seconds(self, sec):
        self.sec = sec

    def minutes(self, min):
        self.min = min


@app.route('/', methods=["GET", "POST"])
def timeVisual():
    form = Form()
    print("="*20)
    print("="*20)
    if form.validate_on_submit():
        print(form.data)    
    return render_template("timerpage.html", form=form)

timer = Timer()

def start(min, sec):
    if min == None:
        min = 0
    if sec == None:
        sec = 10
    timer.seconds(sec)
    timer.minutes(min)
    timer.time()

@app.route('/race')
def race():
    if(timer.min == 0 and timer.sec == 0 and timer.ms == 1):
        timer.reset()
        whowon = timer.winner()
        print("inside route ", whowon)
        return render_template("racepage.html", whowon=whowon)
    return render_template("racepage.html", timer=f'{timer}')



@app.route("/fillin", methods=["POST"])
def fillin():
    form = Form()
    if form:
        min = form.data["min"]
        sec = form.data["sec"]
        start(min, sec)
        return redirect("/race")

