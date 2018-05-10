import requests
import hashlib
import random
import json

def mining(difficulty,previous_hash):
    num = 0
    while True:
        num = random.randint(0,9999999999)
        hashstr = sha2str((previous_hash+str(num)).encode())
        for i in range(difficulty):
            if hashstr[i] != '0':
                break
        break
    return num

def sha2str(encoded_str, hash_func=hashlib.sha3_256):
    return hash_func(encoded_str).hexdigest()


if __name__=='__main__':
    URL = 'http://47.104.190.254:10086'
    response = requests.get(URL+'/chain/lastblock')
    response = response.json()
    difficulty = response['difficulty']
    block_height = response['index']
    previous_hash = response['previous_hash']
    num = mining(difficulty,previous_hash)
    response = requests.get(f'{URL}/mine/{block_height}/{num}')

    print(response.json())



