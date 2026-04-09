import requests
from user_agent import generate_user_agent
from time import sleep
import random
from colorama import Fore, init
import threading
init(autoreset=True)
print(f'''
{Fore.CYAN}
░▀▄░░▄▀
▄▄▄██▄▄▄▄▄░▀█▀▐░▌
█▒░▒░▒░█▀█░░█░▐░▌
█░▒░▒░▒█▀█░░█░░█
█▄▄▄▄▄▄███══════    
{Fore.YELLOW}TikTok Share Tool - Telegram : https://xfff00.t.me - @hyy_yy
''')
class SHARES():
    def __init__(self):
        self.dn, self.bad = 0, 0
        self.proxies_list = []
        self.sources = {
            "http": [
                "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http"
            ],
            "https": [
                "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/https.txt",
                "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https"
            ]
        }
        
        self.fetch_proxies()
        
        self.sess = input(" « + » Enter session (sessionid) : ")
        self.usersa = input(" « + » Enter Target Username : ")
        self.amount = int(input(' « ? » How many shares? '))
        
        self.get_room_info()

    def fetch_proxies(self):
        print(f"{Fore.WHITE}[...] جاري جلب البروكسيات...")
        for proto, urls in self.sources.items():
            for url in urls:
                try:
                    res = requests.get(url, timeout=5)
                    if res.status_code == 200:
                        for line in res.text.splitlines():
                            if ":" in line:
                                self.proxies_list.append({proto: f"{proto}://{line.strip()}"})
                except: continue
        print(f"{Fore.GREEN} « ✓ » Total Proxies: {len(self.proxies_list)}")

    def get_room_info(self):
        headers = {
            "Cookie": f"sessionid={self.sess};",
            "User-Agent": generate_user_agent(),
        }
        try:
            url = f"https://www.tiktok.com/api-live/user/room/?aid=1988&uniqueId={self.usersa}"
            rez = requests.get(url, headers=headers).json()
            self.room = rez["data"]["user"]["roomId"]
            self.owner_id = rez["data"]["user"]["id"]
            print(f"{Fore.GREEN} « ✓ » Room ID: {self.room} | Owner ID: {self.owner_id}")
        except:
            print(f"{Fore.RED} [!] خطأ في جلب بيانات البث. تأكد من اليوزر أو السشن.")
            exit(0)

    def send_share(self):
        url = "https://webcast.tiktok.com/webcast/room/share/"
        params = {
            "aid": "1988",
            "device_platform": "web_pc",
            "room_id": self.room,
        }
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": generate_user_agent()
        }
        cookies = { "sessionid": self.sess, "sessionid_ss": self.sess }
        json_data = { "room_id": str(self.room), "target_id": str(self.owner_id), "share_type": 2 }
        
        proxy = random.choice(self.proxies_list) if self.proxies_list else None
        
        try:
            req = requests.post(url, params=params, headers=headers, json=json_data, cookies=cookies, proxies=proxy, timeout=7)
            if req.status_code == 200:
                self.dn += 1
            else:
                self.bad += 1
            print(f'\r[{Fore.CYAN}Share{Fore.RESET}] {Fore.GREEN}Success [{self.dn}]{Fore.RESET} | {Fore.RED}Fail [{self.bad}]{Fore.RESET}', end='')
        except:
            self.bad += 1

    def start(self):
        threads = []
        for _ in range(self.amount):
            while threading.active_count() > 50:
                sleep(0.1)
            t = threading.Thread(target=self.send_share)
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        print(f"\n\n{Fore.YELLOW} Done! Total Shares Sent: {self.dn}")

if __name__ == '__main__':
    tool = SHARES()
    tool.start()
