from os import system
import threading

threading.Thread(target=system, args=('cd MadadChat && python3.8 BotWeb.py',)).start()
threading.Thread(target=system, args=('cd MadadAi && python3.8 Web_Api.py',)).start()
threading.Thread(target=system, args=('cd MadadAi && python3.8 FormAction.py',)).start()
threading.Thread(target=system, args=('cd MadadGame && python3.8 Game.py',)).start()
threading.Thread(target=system, args=('cd MadadGames/2048_1234 && python3.8 Game.py',)).start()
threading.Thread(target=system, args=('cd MadadGames/emoji_1235 && python3.8 Game.py',)).start()
threading.Thread(target=system, args=('cd MadadGames/tower_block_1233 && python3.8 Tower.py',)).start()
threading.Thread(target=system, args=('cd MadadSite && python3.8 Web.py',)).start()

