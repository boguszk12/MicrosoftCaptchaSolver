import requests, base64, os, time

def getLastId():
    ids = sorted([int(file.split('.')[0]) for file in os.listdir('trainingCaptchas')])
    print(ids)
    if ids == []:
        return 0
    else:
        return ids[-1]



def saveBase(base_string,captcha_id):
    decoded_data=base64.b64decode((base_string))
    with open(f"trainingCaptchas/{captcha_id}.png","wb") as raw: raw.write(decoded_data)


def getRandomCaptcha():
    headers = {
        'authority': 'mybusinessservice.surface.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,de;q=0.6',
        'referer': 'https://mybusinessservice.surface.com/en-US/CheckWarranty/CheckWarranty',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'challengeType': 'visual',
    }

    response = requests.get(
        'https://mybusinessservice.surface.com/Warranty/GetOrRefreshCaptchaChallenge',
        params=params,
        headers=headers,
    )
    try:
        response.json()
        print(response.status_code)
    except:
        print('Timeout')
        return False
    return response.json()['challengeString']


captchaId = getLastId()
print(captchaId)

while True:
    base_string = getRandomCaptcha()
    if base_string == False:
        time.sleep(3)
        continue
    saveBase(base_string,captchaId)
    captchaId+=1
    