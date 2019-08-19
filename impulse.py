#!/usr/bin/env python

import sqlite3
import urllib
import urllib2

with open('hosts/hosts') as f:
    hosts = f.readlines()
hosts = [x.strip() for x in hosts]

with open('hosts/endpoints') as f:
    endpoints = f.readlines()
endpoints = [x.strip() for x in endpoints]

def createDB():
    try:
        db = sqlite3.connect('db/impulse')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS
            hosts(host TEXT PRIMARY KEY, status INTEGER)''')
        db.commit()

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

def saveHosts( hosts ):
    try:
        db = sqlite3.connect('db/impulse')
        cursor = db.cursor()
        for host in hosts:
            cursor.execute('''SELECT * FROM hosts''')
            dbHosts = []
            for row in cursor:
                if row[0] not in hosts:
                    cursor.execute('''DELETE FROM hosts WHERE host = ?''', (row[0],))
                    db.commit()
                else:
                    dbHosts.append(row[0])

            for host in hosts:
                if host not in dbHosts:
                    cursor.execute('''INSERT INTO hosts (host) VALUES(?)''', (host,))
                    db.commit()

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

def notifyChange( host, status, message):
    for endpoint in endpoints:
        data = urllib.urlencode({ 'host': host, 'status': status, 'message': message })
        request = urllib2.Request(endpoint, headers={'User-Agent': 'Impulse Endpoint Checker 0.1'}, data=data)
        response = urllib2.urlopen(request)

def updateHostStatus( host, status, message ):
    try:
        db = sqlite3.connect('db/impulse')
        cursor = db.cursor()
        cursor.execute('''SELECT status FROM hosts WHERE host = ? LIMIT 1''', (host,))
        for row in cursor:
            if (row[0] != status):
                cursor.execute('''UPDATE hosts SET status = ? WHERE host = ?''', (status, host))
                db.commit()
                notifyChange( host, status, message )

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

def checkHosts( hosts ):
    for host in hosts:
        try:
            request = urllib2.Request(host, headers={'User-Agent': 'Impulse Endpoint Checker 0.1'})
            status = urllib2.urlopen(request).getcode()
            updateHostStatus( host, status, '' )
            
        except urllib2.HTTPError as e:
            status = e.code
            updateHostStatus( host, status, e.reason )

        except urllib2.URLError as e:
            status = 0
            updateHostStatus( host, status, e.reason )

createDB()
saveHosts(hosts)
checkHosts(hosts)
