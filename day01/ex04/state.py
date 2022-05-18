import sys

def guess_capital(capital):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	#if state in states:
	#	print(capital_cities[states[state]])
	if capital in capital_cities.values():
		print(states[capital_cities[capital]])
	else:
		print("Unknown state")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit
	else:
		guess_capital(sys.argv[1])
