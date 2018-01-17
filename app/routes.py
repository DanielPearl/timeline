# routes.py

from flask import render_template, redirect, request, url_for
from app import app
import random
from random import randint
from .models import *
from .queries import *
from .forms import *
from .attributes import *
from .timeline import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = None

    timeline = timeline_dict()
    # timeline = get_ancient_history()
    event1 = random.choice(timeline)
    event2 = random.choice(timeline)
    correct = False

    while event2 == event1:
        event2 = random.choice(timeline)

    # --- GET ---
    content = {"form": form, "timeline": timeline, "event1":event1, "event2":event2}
    return render_template('index.html', content=content)
