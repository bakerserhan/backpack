# coding=utf-8
import datetime
from flask import render_template, redirect, url_for, request
from journal import app

@app.route('/')
def home():
    return render_template('index.html')