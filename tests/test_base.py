import simplejson as json

def create_new_item(client, url, data):
    return client.post(url, data=json.dumps(data), content_type='application/json')

def edit_item(client, url, data):
    return client.patch(url, data=json.dumps(data), content_type='application/json')

def delete_item(client, url):
    return client.delete(url)

def get_item(client, url):
    return client.get(url)
