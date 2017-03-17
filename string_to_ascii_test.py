def getStringValue(s):
	values = [ord(c) for c in s]

	return sum(values)


print(getStringValue("hi"))