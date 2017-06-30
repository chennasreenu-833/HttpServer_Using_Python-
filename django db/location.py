import requests
import sqlite3

conn=sqlite3.connect('db.sqlite3')
cursor=conn.execute("SELECT constituency from polling_polltable")
for row in cursor:
    try:
        data=str(row[0])
        try:
            parts=data.split('(',1)
            cont=parts[0]
        except IOError:
            cont = data
        try:
            parts = data.split('-', 1)
            cont = parts[0]
        except IOError:
            cont=data
        payload={'address':cont}
        r=requests.get("https://maps.googleapis.com/maps/api/geocode/json",params=payload)
        json_data=r.json()
        res_data=json_data["results"]
        rand=res_data[0]
        geo_data=rand["geometry"]
        loc_data=geo_data["location"]
        lat=loc_data["lat"]
        long=loc_data["lng"]
        conn.execute("INSERT INTO polling_location(constituency,latitude,longitude) VALUES(?,?,?)",(str(data),lat,long))
        conn.commit()
    except IndexError:
        pass

conn.close()

