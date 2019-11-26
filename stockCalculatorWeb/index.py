import json
import requests
from flask import render_template, Flask
from flask import request
from requests.exceptions import ConnectionError

app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"


@app.route("/ajax", methods=['POST','GET'])
def listener():

	
	tickerSymbol = request.form['tickerSymbol'];
	tickerSymbol = tickerSymbol.upper()
	requestURL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+tickerSymbol+"&apikey=SAXSAL4YOY102RDD"
	r = ''

	try:
		r = requests.get(requestURL)
	except ConnectionError as e:
		return 'Cannot connect to API.'

	if r.status_code != 200 :
		return 'Bad request'

	data = r.json()
	

	if 'Error Message' in data :
		return 'Invalid Stock code'

	val = list(data['Time Series (Daily)'].values())
	data['latest'] = val[0]
	data['latest']['current'] = float(val[0]['4. close'])
	
	sopen = float(val[1]['4. close']) 
	sclose = float(val[0]['4. close'])

	data['latest']['1. open'] = val[1]['4. close']
	# end of morning stock value

	net = round(sclose - sopen,3)

	if net < 0 :
		data['latest']['sign'] = '-'
	elif net >= 0 : 	
		data['latest']['sign'] = '+'

	data['latest']['net'] = abs(net)
	data['latest']['percent'] = round(abs((net/sopen) * 100),3)
	

	# get company information

	jobs = [{"idType":"TICKER", "idValue":tickerSymbol}]

	openfigi_headers = {'Content-Type': 'text/json'}
	openfigi_headers['X-OPENFIGI-APIKEY'] = "bdb67ff0-a8a1-4a2c-98a3-49398ec68a53"
	openfigi_url = 'https://api.openfigi.com/v1/mapping'

	res = requests.post(url=openfigi_url, headers=openfigi_headers,data=json.dumps(jobs))

	data['cname'] = res.json()
	data['cname'] = data['cname'][0]['data'][0]['name']

	return render_template('result.html',stock=data);


@app.route("/", methods=['POST', 'GET'])
def index():
	
	return render_template('form.html')


app.debug = True
app.run()
