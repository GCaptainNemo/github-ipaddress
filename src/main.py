from bs4 import BeautifulSoup
import requests
import re
import os

URL_github = "https://github.com.ipaddress.com/"
URL_fastly = "https://fastly.net.ipaddress.com/github.global.ssl.fastly.net"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def main():
    github_ip = get_github_ip()
    fast_ip = get_fast_ip()
    # print(fast_ip)
    hosts_dir = r"C:\Windows\System32\drivers\etc\hosts"
    github_regex = re.compile(r'github.com', re.I)
    fast_regex = re.compile(r'github.global.ssl.fastly.net', re.I)
    with open(hosts_dir, "r", encoding='utf-8') as f:
        file_data = ""
        git_num = 0
        fast_num = 0
        substitute_fast = str(fast_ip) + " github.global.ssl.fastly.net " + "\n"
        substitute_github = str(github_ip) + " github.com" + "\n"
        for line in f:
            if github_regex.search(line) and git_num == 0:
                file_data += substitute_github
                git_num += 1
            elif fast_regex.search(line) and fast_num == 0:
                file_data += substitute_fast
                fast_num += 1
            else:
                file_data += line
        if git_num == 0:
            file_data += substitute_github
        if fast_num == 0:
            file_data += substitute_fast
        print(file_data)

    with open(hosts_dir, 'w', encoding='utf-8') as f:
        # "w"会覆盖文件
        f.write(file_data)

    # 调出命令行，flushdns
    os.system("ipconfig /flushdns")


def get_github_ip():
    response = requests.get(URL_github, headers=headers)
    response.encoding = 'utf-8'
    SOUP = BeautifulSoup(response.text, 'html.parser')
    trTags = SOUP.find_all("ul", attrs={"class": "comma-separated"})
    ip = trTags[0].text
    return ip

def get_fast_ip():
    response = requests.get(URL_fastly, headers=headers)
    response.encoding = 'utf-8'
    SOUP = BeautifulSoup(response.text, 'html.parser')
    trTags = SOUP.find_all("ul", attrs={"class": "comma-separated"})
    ip = trTags[0].text
    return ip

if __name__ == "__main__":
    main()