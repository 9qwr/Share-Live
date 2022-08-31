import requests
from user_agent import generate_user_agent
from time import time, sleep
import random
from colorama import Fore
import threading
print(f'''

░▀▄░░▄▀
▄▄▄██▄▄▄▄▄░▀█▀▐░▌
█▒░▒░▒░█▀█░░█░▐░▌
█░▒░▒░▒█▀█░░█░░█
█▄▄▄▄▄▄███══════

 {Fore.YELLOW}Telegram{Fore.RESET} : {Fore.CYAN}https://t.me/ik48x
''')
class KAITO():
    def __init__(self):
        self.dn,self.bad,self.pb=0,0,0
        #self.proxy=[]
        self.print_console(" If you are facing a problem, please contact the developer on snapchat @j4s_8 ..")
        self.sess=input("  « + » Enter session : ")
        self.usersa=input(" « + » Enter user name : ")
        self.added = 0
        self.Channel     = ["tiktok_web", "googleplay", "App%20Store"]
        self.Platforms   = ["android", "windows", "iphone", "web" , "web_pc"]
        self.lock = threading.Lock()
        self.amount = int(input(' « ? » How many shares do you want? '))
        self.get_roomid()
    def print_console(self, arg, status = "Console"):
        print(f"\n   {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def update_title(self):
        while self.added == 0:
            sleep(0.2)

        while self.added < self.amount:
            print('Added: {0}/{1}'.format(self.added, self.amount))
            sleep(0.2)

        print('Added: {0}/{1}'.format(self.added, self.amount))
    
    def get_roomid(self):
        headers = {
         "Cookie": f"_abck=05C80B079681C174EB755C5A9047B7E0~-1~YAAQ7e9hXrRFOaOCAQAA6Peiuwi+1m/wvh0Sd95YYjXPOZRpu/p1XsU/YbpX0u5ep+6SYGM5Axa2wVs4THSNdNxNS9zjxuxMBNN9DGQQENfIh57R0x4lSb8XWgA7GyB8TlOCzmbW8cOJkpFWAkwERVlwAX7hc88cuKRupEdZHZfx5InhX/un4CY3jVBVWEIgRKBNhfDBAfmc+UgcMmBbXFWg5IMiae8GMsDSPdeqyj8MLZle8EK6JpGqwiJ+PZ98UVHkDh3OzLBTRHlJpDKlpsoPGbgsYKrhLB2Z34BrMGlQojzLw8x6sOxHewEUhK5xanPH9lepQOKdg2eUBGqSxZSayNjMOpVCAFis133Fb4rXt5xOI9riszJFWgvTxZraYVVI1c6pM4GYpdM=~-1~-1~-1; ttwid=1%7C2qXf0NJ_8TEBHo0ciOwwkxVID_CxHCxfn2CJu3PaNG8%7C1661007783%7C4da417974c8fa5af103614e2f2e54eb64fe6e0c8446510311854b0c2a13e7443; _tt_covid_banner_closed=1; msToken=4tKkqrfVgaDb8DlU5F1WvJ8fBM4sejc9g2yMtVf_3BC59dwYANq2pTYSWPWMIOsz8kWO200qKaljJXMwwd-e-gQfQivz7OWjl8dJMSUZw3IHYLGEVbT4UvrHi-dNrSeMZF9w; tt_csrf_token=vyflaj82-Teur62dgDffmytMjXIxV_fO1B8Y; ak_bmsc=DF57974038A4C80578F35B8B2F7DD814~000000000000000000000000000000~YAAQxe9hXvfriqyCAQAAzlPHuxCZIUqtwnNk/PYipRpXb1wKBZ2ZfG/nDsDdIkBLysFF3V+cQkNPIEGqoXCxW7fUrb+IjgF859np2FZyGqLaEUhoR4aCmjw6ew7B2UODc3yh36kCpsaw7R7zC8qbwuOBlVHz9nVCxM36Hn2tRxWZv2F1SWnhd7+7nH3N1rfZM5WNdKA0aeIf3TfuRCwBVTmqOGq+N0Wu/GIGSwW09AZrfkZNyAXB5vYqi4RAp6R6xonYZlYbYWciF5kotJkd/KPPWhgc1sm/n+tYqVfjp6f+1EdNkPv/aRhJe7l+VUkINPn8wERFd0waIPyONckZtfTbEFZCXp5ylgpk0ZX1Ay7+wDRJCaMju1CRSHX+/mbP+fye6BOUuE+QS4jpCVJ+Wz8V2dN2V9rYE+7CmpbQrem7Bfnvp3zuliYBoHn1E2SB; bm_sz=AEBF4DA688161F9056A51B8D95790C42~YAAQ7e9hXrdFOaOCAQAA6PeiuxBHnHy28yMrfO0uHDpUAz+tpTr9qJhG+VW8JHcKqv10Yl3ed73Q4X9PToZPWFjdYVr3YjVSomcy9pgWDmqz3gNH5ssXabXuINuHIv7Vcj8mgFNLdlSzfXXgxW4jNWZ88QVF3PiV/D1AHwa3Pn+Wi9OIIqEAu9akYy/WjDsIXeJODYUSvYsTjR+M47d+veSK48Oqf3ggWA5sE7Y6jRej7HcGeN4im4GC0VO+y2+2CCPH3/CTI7kWJL20Ds8+V9PI4vOhTsS46Oh2LDZhjkLPhFo=~4534329~4469808; csrf_session_id=ff9a2e80a062531ee613a3c5035ab22d; bm_sv=D35DCD89570EBA72D0DE7ED8376EF748~YAAQ3e9hXkvgNaOCAQAALDzFuxAi1nMtjJBaMnVbDLA5g/6o8KBYCnm2AmQL3jw/nNDsfPHj+nocz3Wdmctg8tmmDOiUAu3zRhkYBG1UPDzlUF2cr3tYc6KMVq0+p/OG+Jgng780ohY5deyxgoXTFiMSR1eofkrfbwVZiS/5gNqEBW2qY5OWwjC+986AH7k3yGLRMrjfS8nsA3Gs9JLXG1jRMqHBMzf3cJpujbtj8mtq2dV/vD7jskE9rUjeY8bzlw==~1; passport_csrf_token=142ec4b7a7044cdbb6b59565f5b83ea8; passport_csrf_token_default=142ec4b7a7044cdbb6b59565f5b83ea8; s_v_web_id=verify_l71zqvs2_YCWVL2JM_1nvE_4oRk_8FnT_X2jkG5zAgQIK; bm_mi=827B8D45DCF4D9A9123D4222B8D1A780~YAAQ3e9hXibgNaOCAQAAmBvFuxB14MytETRuEOX80dRW7ZrhJoQ5k5HqNjG84KMQAXMPe8XLuT04QpERKaq7apAAdxzA5FqcwaXSVJ7wn8nKJedwyJ/SbJVA/rvQ9LS6S12DY5P/moBD3RZBvVjITm3rzqC1ujZmqB8xV/1Sd+hRVepvOfjf+0U+NpahDyWe6Gnj9lj2OpxW+6X5N+I9yaTyBzYPdVUb5Uxfc0MPasZ4DgNEuS3qupatPnKuIuUaMMoPxffUwhCl0jJyoyntmYeFnj9nrqpyOcBRj/w4NPFwsyZFAYifS2eOfEvJGLSMVMERrPXMN0jaTNg2~1; cookie-consent=%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22; odin_tt=4724e3abe4b96126f04d29e398cfbeed959da8118e140d6d302ae36653b80458143ac568cdb1b8365746f2ccdbe9d4195750ba0d80e48cdf5e8ed22369e99c87a37a55e202da924031990315d98caea8; cmpl_token=AgQQAPO_F-RO0rJxGTcZ6t04-JDRmasIf4A0YMXylQ; sid_guard={self.sess}%7C1661005518%7C5184000%7CWed%2C+19-Oct-2022+14%3A25%3A18+GMT; uid_tt=1ee9cd0d2fefcde0e55b49187afd72d2aef1b1030f0cd356bed6269bab701b5a; uid_tt_ss=1ee9cd0d2fefcde0e55b49187afd72d2aef1b1030f0cd356bed6269bab701b5a; sid_tt={self.sess}; sessionid={self.sess}; sessionid_ss={self.sess}; sid_ucp_v1=1.0.0-KGIxMmIxMzdkOGQ3ZDliYzNlYTg1ODVkNjU2MmYyNDYyN2NmNTE5OGEKIAiBiOCOifL9p2IQzt2DmAYYswsgDDC477-SBjgHQPQHEAMaBm1hbGl2YSIgYmRmNDIyNmRmYjgwMTIwYTQzMzA5MjllMzFjYWNhNzU; ssid_ucp_v1=1.0.0-KGIxMmIxMzdkOGQ3ZDliYzNlYTg1ODVkNjU2MmYyNDYyN2NmNTE5OGEKIAiBiOCOifL9p2IQzt2DmAYYswsgDDC477-SBjgHQPQHEAMaBm1hbGl2YSIgYmRmNDIyNmRmYjgwMTIwYTQzMzA5MjllMzFjYWNhNzU; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; csrfToken=8cAqqxBZ_N6QnwsaxoO1sd4b",
         "User-Agent": generate_user_agent(),
         "Accept": "*/*",
         "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
         "Accept-Encoding": "gzip, deflate",
         "Referer": "https://www.tiktok.com/@kaito/live",
         "Sec-Fetch-Dest": "empty",
         "Sec-Fetch-Mode": "cors",
         "Sec-Fetch-Site": "same-origin",
         "Te": "trailers",}
        rez = requests.get(f"https://www.tiktok.com/api-live/user/room/?aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%29&channel=tiktok_web&cookie_enabled=true&device_id=7129559580162868738&device_platform=web_pc&focus_state=true&from_page=user&history_len=7&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=SA&referer=https%3A%2F%2Fwww.tiktok.com%2Fforyou%3Flang%3Dar&region=US&root_referer=https%3A%2F%2Fwww.tiktok.com%2F&screen_height=768&screen_width=1366&sourceType=54&tz_name=Asia%2FRiyadh&uniqueId={self.usersa}&verifyFp=verify_l71zqvs2_YCWVL2JM_1nvE_4oRk_8FnT_X2jkG5zAgQIK&webcast_language=ar",headers=headers).json()
        try:
            self.room = rez["data"]["user"]["roomId"]
        except:
            self.print_console("Something went wrong, contact the developer ...")
            exit(0)
    
    def sent_share(self):
        device_id = str(random.randint(1000000000000000000, 9999999999999999999))
        Headers = {
        	"Cookie": f"_abck=05C80B079681C174EB755C5A9047B7E0~-1~YAAQ7e9hXrRFOaOCAQAA6Peiuwi+1m/wvh0Sd95YYjXPOZRpu/p1XsU/YbpX0u5ep+6SYGM5Axa2wVs4THSNdNxNS9zjxuxMBNN9DGQQENfIh57R0x4lSb8XWgA7GyB8TlOCzmbW8cOJkpFWAkwERVlwAX7hc88cuKRupEdZHZfx5InhX/un4CY3jVBVWEIgRKBNhfDBAfmc+UgcMmBbXFWg5IMiae8GMsDSPdeqyj8MLZle8EK6JpGqwiJ+PZ98UVHkDh3OzLBTRHlJpDKlpsoPGbgsYKrhLB2Z34BrMGlQojzLw8x6sOxHewEUhK5xanPH9lepQOKdg2eUBGqSxZSayNjMOpVCAFis133Fb4rXt5xOI9riszJFWgvTxZraYVVI1c6pM4GYpdM=~-1~-1~-1; ttwid=1%7C2qXf0NJ_8TEBHo0ciOwwkxVID_CxHCxfn2CJu3PaNG8%7C1661007783%7C4da417974c8fa5af103614e2f2e54eb64fe6e0c8446510311854b0c2a13e7443; _tt_covid_banner_closed=1; msToken=4tKkqrfVgaDb8DlU5F1WvJ8fBM4sejc9g2yMtVf_3BC59dwYANq2pTYSWPWMIOsz8kWO200qKaljJXMwwd-e-gQfQivz7OWjl8dJMSUZw3IHYLGEVbT4UvrHi-dNrSeMZF9w; tt_csrf_token=vyflaj82-Teur62dgDffmytMjXIxV_fO1B8Y; ak_bmsc=DF57974038A4C80578F35B8B2F7DD814~000000000000000000000000000000~YAAQxe9hXvfriqyCAQAAzlPHuxCZIUqtwnNk/PYipRpXb1wKBZ2ZfG/nDsDdIkBLysFF3V+cQkNPIEGqoXCxW7fUrb+IjgF859np2FZyGqLaEUhoR4aCmjw6ew7B2UODc3yh36kCpsaw7R7zC8qbwuOBlVHz9nVCxM36Hn2tRxWZv2F1SWnhd7+7nH3N1rfZM5WNdKA0aeIf3TfuRCwBVTmqOGq+N0Wu/GIGSwW09AZrfkZNyAXB5vYqi4RAp6R6xonYZlYbYWciF5kotJkd/KPPWhgc1sm/n+tYqVfjp6f+1EdNkPv/aRhJe7l+VUkINPn8wERFd0waIPyONckZtfTbEFZCXp5ylgpk0ZX1Ay7+wDRJCaMju1CRSHX+/mbP+fye6BOUuE+QS4jpCVJ+Wz8V2dN2V9rYE+7CmpbQrem7Bfnvp3zuliYBoHn1E2SB; bm_sz=AEBF4DA688161F9056A51B8D95790C42~YAAQ7e9hXrdFOaOCAQAA6PeiuxBHnHy28yMrfO0uHDpUAz+tpTr9qJhG+VW8JHcKqv10Yl3ed73Q4X9PToZPWFjdYVr3YjVSomcy9pgWDmqz3gNH5ssXabXuINuHIv7Vcj8mgFNLdlSzfXXgxW4jNWZ88QVF3PiV/D1AHwa3Pn+Wi9OIIqEAu9akYy/WjDsIXeJODYUSvYsTjR+M47d+veSK48Oqf3ggWA5sE7Y6jRej7HcGeN4im4GC0VO+y2+2CCPH3/CTI7kWJL20Ds8+V9PI4vOhTsS46Oh2LDZhjkLPhFo=~4534329~4469808; csrf_session_id=ff9a2e80a062531ee613a3c5035ab22d; bm_sv=D35DCD89570EBA72D0DE7ED8376EF748~YAAQ3e9hXkvgNaOCAQAALDzFuxAi1nMtjJBaMnVbDLA5g/6o8KBYCnm2AmQL3jw/nNDsfPHj+nocz3Wdmctg8tmmDOiUAu3zRhkYBG1UPDzlUF2cr3tYc6KMVq0+p/OG+Jgng780ohY5deyxgoXTFiMSR1eofkrfbwVZiS/5gNqEBW2qY5OWwjC+986AH7k3yGLRMrjfS8nsA3Gs9JLXG1jRMqHBMzf3cJpujbtj8mtq2dV/vD7jskE9rUjeY8bzlw==~1; passport_csrf_token=142ec4b7a7044cdbb6b59565f5b83ea8; passport_csrf_token_default=142ec4b7a7044cdbb6b59565f5b83ea8; s_v_web_id=verify_l71zqvs2_YCWVL2JM_1nvE_4oRk_8FnT_X2jkG5zAgQIK; bm_mi=827B8D45DCF4D9A9123D4222B8D1A780~YAAQ3e9hXibgNaOCAQAAmBvFuxB14MytETRuEOX80dRW7ZrhJoQ5k5HqNjG84KMQAXMPe8XLuT04QpERKaq7apAAdxzA5FqcwaXSVJ7wn8nKJedwyJ/SbJVA/rvQ9LS6S12DY5P/moBD3RZBvVjITm3rzqC1ujZmqB8xV/1Sd+hRVepvOfjf+0U+NpahDyWe6Gnj9lj2OpxW+6X5N+I9yaTyBzYPdVUb5Uxfc0MPasZ4DgNEuS3qupatPnKuIuUaMMoPxffUwhCl0jJyoyntmYeFnj9nrqpyOcBRj/w4NPFwsyZFAYifS2eOfEvJGLSMVMERrPXMN0jaTNg2~1; cookie-consent=%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22; odin_tt=4724e3abe4b96126f04d29e398cfbeed959da8118e140d6d302ae36653b80458143ac568cdb1b8365746f2ccdbe9d4195750ba0d80e48cdf5e8ed22369e99c87a37a55e202da924031990315d98caea8; cmpl_token=AgQQAPO_F-RO0rJxGTcZ6t04-JDRmasIf4A0YMXylQ; sid_guard={self.sess}%7C1661005518%7C5184000%7CWed%2C+19-Oct-2022+14%3A25%3A18+GMT; uid_tt=1ee9cd0d2fefcde0e55b49187afd72d2aef1b1030f0cd356bed6269bab701b5a; uid_tt_ss=1ee9cd0d2fefcde0e55b49187afd72d2aef1b1030f0cd356bed6269bab701b5a; sid_tt={self.sess}; sessionid={self.sess}; sessionid_ss={self.sess}; sid_ucp_v1=1.0.0-KGIxMmIxMzdkOGQ3ZDliYzNlYTg1ODVkNjU2MmYyNDYyN2NmNTE5OGEKIAiBiOCOifL9p2IQzt2DmAYYswsgDDC477-SBjgHQPQHEAMaBm1hbGl2YSIgYmRmNDIyNmRmYjgwMTIwYTQzMzA5MjllMzFjYWNhNzU; ssid_ucp_v1=1.0.0-KGIxMmIxMzdkOGQ3ZDliYzNlYTg1ODVkNjU2MmYyNDYyN2NmNTE5OGEKIAiBiOCOifL9p2IQzt2DmAYYswsgDDC477-SBjgHQPQHEAMaBm1hbGl2YSIgYmRmNDIyNmRmYjgwMTIwYTQzMzA5MjllMzFjYWNhNzU; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; csrfToken=8cAqqxBZ_N6QnwsaxoO1sd4b",
        	"User-Agent": generate_user_agent(),
        	"Accept": "*/*",
        	"Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
        	"Accept-Encoding": "gzip, deflate",
        	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        	"X-Secsdk-Csrf-Token": "0001000000018957afd4c2d82d4524b7d8b84dbc451335ac832eedabac86a301779e102dcb39170d15c74209469a",
        	"Content-Length": "0",
        	"Sec-Fetch-Dest": "empty",
        	"Sec-Fetch-Mode": "cors",
        	"Sec-Fetch-Site": "same-site",
        	"Te": "trailers",
        	"Connection": "close",
        	}
        try:
            platform = random.choice(self.Platforms)
            appName = random.choice(["tiktok_web", "musically_go"])
            osVersion = random.randint(1, 12)
            channelLol = random.choice(self.Channel)
            req = requests.post(f"https://webcast.tiktok.com/webcast/room/share/?aid=1988&app_language=ar&app_name={appName}&browser_language=ar&browser_platform={platform}&browser_version={osVersion}&channel={channelLol}&cookie_enabled=true&device_id={device_id}&device_platform={platform}&room_id={self.room}&share_type=2",headers=Headers,stream=True)
            if '"status_code":0' in req.text:
                self.dn +=1
                print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Share [{self.dn}]{Fore.RESET} | {Fore.RED}Error Share [{self.bad}]{Fore.RESET} | {Fore.CYAN}Target: [{self.usersa}] How many shares [{self.amount}] RoomId [{self.room}]{Fore.RESET}',end='')
            
            elif '""' in req.text:
                self.bad+=1
                print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Share [{self.dn}]{Fore.RESET} | {Fore.RED}Error Share [{self.bad}]{Fore.RESET} | {Fore.CYAN}Target: [{self.usersa}] How many shares [{self.amount}] RoomId [{self.room}]{Fore.RESET}',end='')
                self.lock.acquire()
                print(req.text)
                self.lock.release()
                self.sent_share()
                
            else:
                
                self.bad +=1
                print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Share [{self.dn}]{Fore.RESET} | {Fore.RED}Error Share [{self.bad}]{Fore.RESET} | {Fore.CYAN}Target: [{self.usersa}] How many shares [{self.amount}] RoomId [{self.room}]{Fore.RESET}',end='')
        		
        except:
            print(req.text)
            self.sent_share()
    def start(self):
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.sent_share).start()
                    break

        sleep(3)
if __name__ == '__main__':
    tiktok_share = KAITO()
    tiktok_share.start()
