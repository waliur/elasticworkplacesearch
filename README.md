# About

This is a POC container stack for Elasticsearch Workplace for indexing documents stored on a shared network drive. The built in Workplace Search UI is used to perform searches.


## Docker Containers 

There are 6 containers run by docker-compose:

* **elasticsearch** - Search engine powering Elasticsearch products such as the "ent-search" container.
* **ent-search** - Split into two products: App Search (websites) and Workplace search to index file network file shares (Custom API), Dropbox, Jira, Zendesk etc.
* **kibana** - Explore, Visualize, Discover Data
* **drive-connector** - Runs "[Official Enterprise Search | Workplace Search - Network Drives Connector](https://github.com/elastic/enterprise-search-network-drive-connector)". It reads data stored in a "Samba/SMB shared network drive" and sends the metadata to Elastic Workplace search provided by the "ent-search" container.
* **samba** - Full Linux based Samba share used to simulate a network file share.
* **streamlit** - Python search UI - Experimental and no longer used as ent-search provides a built in search box UI. Container mostly used for testing connection with other containers such as samba server.

### Commands

**Spin up container stack:**
```
docker-compose down; docker-compose up -d ; docker-compose ps
```

U: elastic P: changeme
* Generate API credentials for Workplace search: http://localhost:3002/ws#/org/sources
* Add a "Custom API Source" http://localhost:3002/ws#/org/sources/add/custom
* Note down "Source Identifier" and "Access Token"
* Add "Source Identifier" and "Access Token" to `network_drive_connector.yml`

### Test drive-connector

```
docker exec -it drive-connector /bin/bash
make test_connectivity
```

### Perform full sync

```
ees_network_drive -c network_drive_connector.yml full-sync
```

### Test elastic search connection

```
curl http://localhost:9200/
```
U: elastic P: changeme

### Test Samba network share connection from streamlit container
```
docker exec -it streamlit /bin/bash
ping samba
smbclient -L //samba
```
U: root P: bar

**Mount samba network share directly to streamlit container**
```
mkdir /mnt/samba/
mount -t cifs -o username=q //samba/share1/ /mnt/samba/
```


# Official Enterprise Search | Workplace Search - Network Drives Connector

https://github.com/elastic/enterprise-search-network-drive-connector

### Libraries
https://www.elastic.co/guide/en/enterprise-search/7.17/programming-language-clients.html#programming-language-clients

### Connecting custom sources
https://www.elastic.co/guide/en/workplace-search/7.17/workplace-search-custom-api-sources.html

**Manually populate Workplace search service with document metadata for testing**

Replace `[ID]` and `[Token]` with API keys generated from http://localhost:3002/ws#/org/sources

```
curl -X POST http://localhost:3002/api/ws/v1/sources/[ID]/documents/bulk_create \
-H "Authorization: Bearer [Token]" \
-H "Content-Type: application/json" \
-d '[
  {
    "id" : 1234,
    "title" : "The Meaning of Time Sam Hodge",
    "body" : "Not much. It is a made up thing.",
    "url" : "https://example.com/meaning/of/time",
    "created_at": "2019-06-01T12:00:00+00:00",
    "type": "list"
  },
  {
    "id" : 1235,
    "title" : "The Meaning of Sleep - George Poppy!!!",
    "body" : "Rest, recharge, and connect to the Ether.",
    "url" : "https://example.com/meaning/of/sleep",
    "created_at": "2019-06-01T12:00:00+00:00",
    "type": "list"
  },
  {
    "id" : 1236,
    "title" : "The Meaning of Life - Waliur",
    "body" : "Be excellent to each other.",
    "url" : "https://example.com/meaning/of/life",
    "created_at": "2019-06-01T12:00:00+00:00",
    "type": "list"
  }
]'
```