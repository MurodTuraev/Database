from tinydb import TinyDB
db = TinyDB('db.json')
user1 = {'id': 101, 'first_name': 'Anvar', 'last_name': 'Komilov', 'Birthday': '25.03.1990',
         'Email': 'anvarjon@jmail.com', 'Job': 'Teacher', 'Phone': '+998931234569'}
user2 = {'id': 405, 'first_name': 'Jamila', 'last_name': 'Arslanova', 'Birthday': '02.04.1965',
         'Email': 'star@jmail.com', 'Job': 'Teacher', 'Phone': '+998970200032'}
user3 = {'id': 602, 'first_name': 'Javlon', 'last_name': 'Shukurov', 'Birthday': '01.10.2000',
         'Email': 'javlonbek@jmail.com', 'Job': 'developer', 'Phone': '+998996566666'}
user4 = {'id': 874, 'first_name': 'Djon', 'last_name': 'Snow', 'Birthday': '01.04.1989',
         'Email': 'snow@jmail.com', 'Job': 'actor', 'Phone': '+998974587485'}
user5 = {'id': 302, 'first_name': 'Alisher', 'last_name': 'Nizomov', 'Birthday': '05.12.2001',
         'Email': 'alisher@jmail.com', 'Job': 'writer', 'Phone': '+998995412365'}

db.insert_multiple([user1, user2, user3, user4, user5])
