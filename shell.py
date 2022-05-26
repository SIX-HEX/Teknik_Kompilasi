import basic_FIX

while True:
	text = input('REZA > ')
	if text.strip() == "": continue
	result, error = basic_FIX.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
