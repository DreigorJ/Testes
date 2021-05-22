
class Msg:


	def __init__(self, text, date ):
		self.text = text
		self.date = date

	def separa(msg):
		msg.words = {}
		aux = msg.text.split(" ")
		tmp = []

		msg.countChars = 0
		for i in aux:
			msg.countChars += len(i)

		for i in aux:
			aux_2 = i.split(".")

			if aux_2 == '':
				aux_2 = i
			
			if aux_2 == '':
				continue
			tmp.extend( aux_2 )
		
		aux = tmp
		tmp = []

		for i in aux:
			aux_2 = i.split(",")

			if aux_2 == '':
				aux_2 = i
			
			tmp.extend( aux_2 )
		aux = tmp
		tmp = []

		for i in aux:
			aux_2 = i.split("!")

			if aux_2 == '':
				aux_2 = i
			
			tmp.extend( aux_2 )

		aux = tmp
		tmp = []

		for i in aux:
			aux_2 = i.split(";")

			if aux_2 == '':
				aux_2 = i
			
			tmp.extend( aux_2 )

		aux = tmp
		tmp = []

		for i in aux:
			aux_2 = i.split("(")

			if aux_2 == '':
				aux_2 = i
			
			tmp.extend( aux_2 )

		aux = tmp
		tmp = []

		for i in aux:
			aux_2 = i.split(")")

			if aux_2 == '':
				aux_2 = i
			
			tmp.extend( aux_2 )

		aux = tmp
		count = 0

		for i in aux:
			count += len(i) 
			if(i in msg.words):
				msg.words[i] += 1
			else:
				msg.words[i] = 1

		msg.countCharsEsp = msg.countChars - count

		if('' in msg.words):
			msg.words.pop('')

	def verifica(self, palavra):
		count = 0

		for i in self.words:
			if(self.words[i] == palavra):
				count += 1

		return count

	    ##falta valor de classificação
	    #
	    #
	    #			: / < > "" 


class Ponto:
	def __init__(self, x, y ):
		self.x = x
		self.y = y