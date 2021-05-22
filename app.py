from flask import Flask, render_template, jsonify, request
import pandas as pd

import json
import ujson
import plotly

from datetime import datetime
from functools import lru_cache
import msn
import zreader
import numpy as np

app = Flask(__name__)
app.debug = True

@lru_cache(maxsize=None)	
def carrega_Dataset(path: str, type):

	arq = []
	reader = zreader.Zreader(path, chunk_size=2 ** 26)


	for line in reader.readlines():
		line = ujson.loads(line)		#iterador

		if(type == 1):
			text = line.get("body")
			if not text:			#pula se não tiver texto
				continue

			data = line.get("author_created_utc")
			if not data:			#pula se não tiver texto
				continue
			data = datetime.utcfromtimestamp(data)

			
		else:
			text = line.get("message")
			if not text:			#pula se não tiver texto
				continue

			data = line.get("date")
			if not data:			#pula se não tiver texto
				continue
			data = data.replace('T',' ')
			data = data[:data.index('+')]
			data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
#				data = 0
#			else:
#				data = datetime.utcfromtimestamp(data)

#			value = line.get("views")
#			if not value:			#pula se não tiver texto
#				value = 0
			

		tp = msn.Msg(text, data)
		tp.separa()

		arq.append( tp )



		if len(arq) >= 50:		#contingência_testes
#			print(arq[])
#			print(arq[1].text + " - " + str(arq[1].date))
			break

	return arq


temp1 = carrega_Dataset("Reddit/RC_2019-04.zst", 1)
temp2 = carrega_Dataset("Telegram/messages.ndjson.zst", 2)

dat = temp1 + temp2

#print(dat[1].words)
dados = []

@app.route('/')
def index():

	for i, aux in enumerate( dat ):
		dados.append(
			dict(
				id = i,
				pos = 0,
				menssagem = aux.text,
				date = aux.date,
				words = aux.words,
				countChars = aux.countChars,
				countCharsEsp = aux.countCharsEsp
			)
		)



	# Add "ids" to each of the graphs to pass up to the client
	# for templating
	#ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

	return render_template('layouts/index.html', dados = json.dumps(dados, cls=plotly.utils.PlotlyJSONEncoder))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
