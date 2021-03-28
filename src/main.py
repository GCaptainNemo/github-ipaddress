from bs4 import BeautifulSoup
import requests
import re
import os

_URL_ = "https://github.com.ipaddress.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def main():
    ip = get_ip()
    hosts_dir = r"C:\Windows\System32\drivers\etc\hosts"
    regex = re.compile(r'github.com', re.I)
    with open(hosts_dir, "r", encoding='utf-8') as f:
        file_data = ""
        num = 0
        substitute = "github.com " + str(ip) + "\n"
        for line in f:
            if regex.search(line) and num == 0:
                file_data += substitute
                num += 1
            else:
                file_data += line
        if num == 0:
            file_data += substitute
        print(file_data)

    with open(hosts_dir, 'w', encoding='utf-8') as f:
        # "w"会覆盖文件
        f.write(file_data)

    # 调出命令行，flushdns
    os.system("ipconfig /flushdns")


def get_ip():
    response = requests.get(_URL_, headers=headers)
    response.encoding = 'utf-8'
    SOUP = BeautifulSoup(response.text, 'html.parser')
    trTags = SOUP.find_all("ul", attrs={"class": "comma-separated"})
    ip = trTags[0].text
    return ip


if __name__ == "__main__":
    main()