import requests

def upload_image_to_imgur(image_url):
    client_id = ''
    url = "https://api.imgur.com/3/upload"
    headers = {
        'Authorization': f'Client-ID {client_id}',
    }

    data = {
        'image': image_url,
        'type': 'url',
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_response = response.json()
        image_url = json_response['data']['link']
        return image_url
    else:
        print(f"Error uploading image: {response.status_code}")
        print(response.json())
        return image_url


