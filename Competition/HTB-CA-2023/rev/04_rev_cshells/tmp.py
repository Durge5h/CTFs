from pwn import *


t = b'\x2c\x4a\xb7\x99\xa3\xe5\x70\x78\x93\x6e\x97\xd9\x47\x6d\x38\xbd\xff\xbb\x85\x99\x6f\xe1\x4a\xab\x74\xc3\x7b\xa8\xb2\x9f\xd7\xec\xeb\xcd\x63\xb2\x39\x23\xe1\x84\x92\x96\x09\xc6\x99\xf2\x58\xfa\xcb\x6f\x6f\x5e\x1f\xbe\x2b\x13\x8e\xa5\xa9\x99\x93\xab\x8f\x70\x1c\xc0\xc4\x3e\xa6\xfe\x93\x35\x90\xc3\xc9\x10\xe9'

m2 = b'\x64\x1e\xf5\xe2\xc0\x97\x44\x1b\xf8\x5f\xf9\xbe\x18\x5d\x48\x8e\x91\xe4\xf6\xf1\x5c\x8d\x26\x9e\x2b\xa1\x02\xf7\xc6\xf7\xe4\xb3\x98\xfe\x57\xed\x4a\x4b\xd1\xf6\xa1\xeb\x09\xc6\x99\xf2\x58\xfa\xcb\x6f\x6f\x5e\x1f\xbe\x2b\x13\x8e\xa5\xa9\x99\x93\xab\x8f\x70\x1c\xc0\xc4\x3e\xa6\xfe\x93\x35\x90\xc3\xc9\x10\xe9'

flag = ""

for i in range(77):
	if i < len(t) and i < len(m2):
		flag += chr(t[i]^m2[i])

flag = re.search(r'HTB{.*}', flag).group(0)
print(flag)

