import json, sys

def dicttojson(dicts):
	return json.dumps(dicts,ensure_ascii=False, indent=4, separators=(',', ': '))

if __name__ == '__main__':
	data = dicttojson(sys.argv[1])