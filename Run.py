import os
if __name__ == "__main__":
	try:
		__import__("Public").login()
	except Exception as e:
		exit(str(e))
