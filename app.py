#!/usr/bin/env python

import urllib
import json
import os
import os.path
import sys
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
import logging
import apiai


# Flask app should start in global layout
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():	
	return render_template("index2.html")	

		
	


if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
