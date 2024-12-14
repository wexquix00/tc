import requests

print("""\033[1m\033[92m		⠄⢀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⣀
		⢠⣿⢿⣿⣿⣽⣯⡿⣽⢯⡿⣽⢯⡿⣽⣯⣿⣽⣟⡿⣳
		⡸⡾⢟⣓⡓⠓⠯⠿⣿⣽⡽⣯⣿⡟⠭⠚⠒⠛⠺⢯⢗
		⣞⢵⢯⢟⡿⣷⣶⢀⠈⢹⣿⡋⠄⡀⣴⣶⡿⡿⣻⢪⡪
		⡧⡃⡓⠍⠊⠊⠊⠳⢅⣽⣿⣇⢜⠜⠙⠈⠊⠑⡑⢑⡱
		⣿⣾⣶⣦⣶⣶⣴⣶⡯⣷⣿⡯⣟⣶⣶⣶⣶⣴⣶⣶⣷
		⢫⡻⡽⣫⢿⢽⣻⣳⢿⣽⣿⢯⣻⣞⣯⢿⢽⢯⡻⡝⡟
		⢂⡊⠊⠇⢫⣑⣭⠾⢻⠾⡿⢟⠞⠷⣥⣉⡣⠣⠃⡑⢔
		⠐⢱⣦⠐⢿⣿⣿⣴⡄⠑⠘⠈⢠⣦⣿⡿⣯⠂⣠⡎⠆
		⠄⢈⠿⣌⢄⣀⣀⠄⠄⠠⠖⠄⠄⠄⡀⣀⠄⣰⠟⡑
		⠄⠄⠑⡹⢧⡈⢉⠙⠛⠛⠛⠛⠛⢉⠉⢁⢴⠋⠜
		⠄⠄⠄⠈⠪⣳⡦⡯⣿⡄⠄⢴⣯⣖⢵⡞⡑⠈
		⠄⠄⠄⠄⠄⠄⠻⢾⣿⡅⠄⣽⣿⠾⠩⠄""")
print("	|________________________________|")
print("		developer: t.me/wexquix\n		kanal: t.me/wexquixpython\n	 	Tc sorgu tool\n	|_______________________________|")
tc = input("\n\nTc gir:   ")
api = f"https://api.tsgonline.net/tsgucretsizapi/adpro.php?auth=tsgxyunus&tc={tc}"
response = requests.get(api)
d = response.json()

data = d['data'][0]

print(f"\n\n\033[96m__________________\nad: {data['AD']}")
print(f"gsm: {data['GSM']}")
print(f"baba adı: {data['BABAADI']}")
print(f"Baba tc: {data['BABATC']}")
print(f"anne adı: {data['ANNEADI']}")
print(f"Anne tc: {data['ANNETC']}")
print(f"memleket il: {data['MEMLEKETIL']}")
print(f"medeni hal: {data['MEDENIHAL']}")
print(f"cinsiyet: {data['CINSIYET']}")
print(f"adres il: {data['ADRESIL']}\n__________________")
