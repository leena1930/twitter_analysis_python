import json

with open('python.json' , 'r') as f:
    line = f.readline()   #read only the first tweet/line
    tweet =json.loads(line)  #load it as python dict
    print(json.dumps(tweet , indent =4))  #pretty print