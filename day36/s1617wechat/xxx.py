import re

msg = """window.QRLogin.code = 200; window.QRLogin.uuid = "Idm9DGWY_A==";"""
data = re.findall('uuid = "(.*)";',msg)
print(data[0])