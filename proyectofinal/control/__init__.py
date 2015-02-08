# -*- coding: utf-8 -*-
 
from flask import Flask

control=Flask(__name__)

from control import index
from control import appControl