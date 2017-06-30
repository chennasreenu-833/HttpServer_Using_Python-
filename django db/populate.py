import json
import sqlite3

db=sqlite3.connect('db.sqlite3')
data=json.load(open('dump.json'))
for val in data:
	constituency = val['Constituency']
	constituency_code = val['Constituency-code']
	leading_candidate = val['Leading Candidate']
	leading_party = val['Leading Party']
	trailing_candidate = val['Trailing Candidate']
	trailing_party = val['Trailing Party']
	margin = val['Margin']
	status = val['Status']
	state = val['State']
	state_code = val['State-code']
	db.execute("INSERT INTO polling_polltable(constituency,constituency_code,leading_candidate,leading_party,trailing_candidate,trailing_party,margin,status,state,state_code) VALUES(?,?,?,?,?,?,?,?,?,?)",(str(constituency),constituency_code,str(leading_candidate),str(leading_party),str(trailing_candidate),str(trailing_party),margin,str(status),str(state),str(state_code)))
	db.commit()
db.close()
