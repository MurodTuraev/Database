from tinydb import TinyDB
smartphone = TinyDB('smartphone.json')
s1 = {'id': 1, 'category': 'smartphone', 'company': 'Samsung'}
s2 = {'id': 2, 'category': 'smartphone', 'company': 'Apple'}
s3 = {'id': 3, 'category': 'smartphone', 'company': 'Huawei'}
s4 = {'id': 4, 'category': 'smartphone', 'company': 'Oppo'}
s5 = {'id': 5, 'category': 'smartphone', 'company': 'Xiomi'}

smartphone.insert_multiple([s1, s2, s3, s4, s5])
