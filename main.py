import requests, json, time, os

VK_USER_ID = "51896755"
VK_TOKEN = ''


def get_api_dat(offset=0, count=50):
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'offset': offset,
        'count': count,
        'photo_sizes': 0,
        'v': 5.103
    })
    return json.loads(api.text)


def get_sev():
    data = get_api_dat()
    count_foto = data["response"]["count"]
    i = 0
    count = 50
    fotos = []
    while i <= count_foto:
        if i != 0:
             data = get_api_dat(offset=i, count=count)
         for files in data["response"]["items"]:
             file_url = files["sizes"][-1]["url"]
             filename = file_url.split("/")[-1]
             fotos.append(filename)
             time.sleep(0.1)
             api = requests.get(file_url)

             with open("images/%s" % filename, "wb") as file:
                 file.write(api.content)
         i += count



def main():
    get_sev()


if __name__ == "__main__":
    main()



