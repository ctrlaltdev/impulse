Docker image to check the pulse of hosts

It will check the hosts your provide every minute and will notify you everytime the status of the monitored hosts status change

impulse will send a POST request with info about the status and host for which the status changed.

impulse need 2 files:
- hosts/hosts: that is the list of url you check on (1 per line)
- hosts/endpoints: that is the list of endpoints to notify when something changes (1 per line)

To run: 
```
docker run --name impulse \
  -v "path/to/where/you/store/the/hosts/and/endpoints/files:/impulse/hosts" \
  -v "optionally/path/to/where/the/sqlitedb/will/be/stored:/impulse/db" \
  ctrlaltdev:impulse
```
