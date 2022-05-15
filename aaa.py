#------made by Islam Elshenawy 💓-----------#
#------script to El-Joker ViP------------------------#
#Good luck 

#------------import---------------#
import telebot,time
from telebot import types 
from random import random
import random
from ntpath import join
import bs4
from bs4 import BeautifulSoup
import ssl
import time
from time import sleep
import re
import subprocess
import sys
import requests
import os
import urllib
import pyrebase
import os
import urllib3
import getpass
import requests
from tqdm import tqdm
import math
#-----------------color-----------------#
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
#-----------------color-----------------#

#-----------------firebase-----------------#
print(A+"["+C+"•"+A+"]"+Z+"STARTED 💓💫")
token = "5289833778:AAFxRCm2qT1h2RIqj0V-EuasoiZmh53ELrM"
id_bot = "1791009992"
firebaseConfig = {
    "apiKey": "AIzaSyCZaGvjUlz_fzBpcqG7AGHMhT6zXl7zHF0",
    "authDomain": "startv2-2a68a.firebaseapp.com",
    "projectId": "startv2-2a68a",
    "databaseURL": "https://startv2-2a68a.firebaseio.com",
    "storageBucket": "startv2-2a68a.appspot.com",
    "messagingSenderId": "743024432763",
    "appId": "1:743024432763:web:da4e5680d9c6c9961af4de",
    "measurementId": "G-KEJ980W0HS"
};
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
try:
	#-----------------comander_bein-----------------#
	def restart():
	    print("argv : ", sys.argv)
	    print("sys executable: ", sys.executable)
	    print("restart now!")
	    os.execv(sys.executable, ["python"] + sys.argv)
	
	bot = telebot.TeleBot(token)
	
	@bot.message_handler(commands=['bein'])
	
	def start(message):
	    SE = "1"
	    h_bein = types.InlineKeyboardMarkup()
	    button1 = types.InlineKeyboardButton(text = "bein pre-1-4k", callback_data= "click1")
	    button2 = types.InlineKeyboardButton(text = "bein pre-1-FHD", callback_data= "click2")
	    button3 = types.InlineKeyboardButton(text = "bein pre-1-SD", callback_data= "click3")
	    button4 = types.InlineKeyboardButton(text = "bein pre-2-4k", callback_data= "click4")
	    button5 = types.InlineKeyboardButton(text = "bein pre-2-FHD", callback_data= "click5")
	    button6 = types.InlineKeyboardButton(text = "bein pre-2-SD", callback_data= "click6")
	    button7 = types.InlineKeyboardButton(text = "bein pre-3-4k", callback_data= "click7")
	    button8 = types.InlineKeyboardButton(text = "bein pre-3-FHD", callback_data= "click8")
	    button9 = types.InlineKeyboardButton(text = "bein pre-3-SD", callback_data= "click9")
	    button10 = types.InlineKeyboardButton(text = "bein 1-4k", callback_data= "click10")
	    button11 = types.InlineKeyboardButton(text = "bein 1-FHD", callback_data= "click11")
	    button12 = types.InlineKeyboardButton(text = "bein 1-SD", callback_data= "click12")
	    button13 = types.InlineKeyboardButton(text = "bein 2-4k", callback_data= "click13")
	    button14 = types.InlineKeyboardButton(text = "bein 2-FHD", callback_data= "click14")
	    button15 = types.InlineKeyboardButton(text = "bein 2-SD", callback_data= "click15")
	    button16 = types.InlineKeyboardButton(text = "bein 3-4k", callback_data= "click16")
	    button17 = types.InlineKeyboardButton(text = "bein 3-FHD", callback_data= "click17")
	    button18 = types.InlineKeyboardButton(text = "bein 3-SD", callback_data= "click18")
	    button19 = types.InlineKeyboardButton(text = "bein 4-4k", callback_data= "click19")
	    button20 = types.InlineKeyboardButton(text = "bein 4-FHD", callback_data= "click20")
	    button21 = types.InlineKeyboardButton(text = "bein 4-SD", callback_data= "click21")
	    button22 = types.InlineKeyboardButton(text = "bein 5-4k", callback_data= "click22")
	    button23 = types.InlineKeyboardButton(text = "bein 5-FHD", callback_data= "click23")
	    button24 = types.InlineKeyboardButton(text = "bein 5-SD", callback_data= "click24")
	    button25 = types.InlineKeyboardButton(text = "bein 6-4k", callback_data= "click25")
	    button26 = types.InlineKeyboardButton(text = "bein 6-FHD", callback_data= "click26")
	    button27 = types.InlineKeyboardButton(text = "bein 6-SD", callback_data= "click27")
	    button28 = types.InlineKeyboardButton(text = "El-Joker ViP 💓💫", callback_data= "click28")
	    h_bein.add(button1, button2,button3, button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28)
	    bot.reply_to(message, text="""<strong>💫 Hello Pro : Islam 😇
	💫 Bot El-Joker ViP  
	💫 Ch : @Y_G_U
	💫 Program Bot : Islam El-shenawy 
	</strong>  """, reply_markup=h_bein, parse_mode="html")
	
	    if SE == "1":
	        print ("-----1-----")
	        
	        @bot.callback_query_handler(func=lambda call: True)
		
		
			#----------------------bein_1---------------------------#
		
	        def callback_date(call):
		    
		    
	            if call.data == "click1":
	                key = "-MKkLxOybuawNu1DQwUe"
			        
			  
	            elif call.data == "click2":
	                key = "-MKkLxOybuaJcu1DQwUe"
			        
	            elif call.data == "click3":
	                key = "-MKkLxOybuawNu1jcwUe"
			       
	            elif call.data == "click4":
	                key = "-MKkMTn34-RDB4Qa4Je1"
			      
	            elif call.data == "click5":
	                key = "-MKkMTn34-cjB4Qa4Je1"
			      
	            elif call.data == "click6":
	                key = "-MKkMTn34-dkB4Qa4Je1"
			        
	            elif call.data == "click7":
	                key = "-MKkMhyHh1fsiVHD96BH"
			        
	            elif call.data == "click8":
	                key = "-MKkMhyHh1fgkVHD96BH"
			     
	            elif call.data == "click9":
	                key = "-MKkMhyHh1fssnHD96BH"
			        
	            elif call.data == "click10":
	                key = "-MKkMrkQcdju8tbC2xFP"
			      
	            elif call.data == "click11":
	                key = "-MKkMrkQcdjuvkbC2xFP"
			    
	            elif call.data == "click12":
	                key = "-MKkMrkQcdbx8tbC2xFP"
			        
	            elif call.data == "click13":
	                key = "-MKkN7K55g5E79EsJjZ5"
			       
	            elif call.data == "click14":
	                key = "-MKkN7K55g5EchEsJjZ5"
			      
	            elif call.data == "click15":
	                key = "-MKkN7K55nsE79EsJjZ5"
			      
	            elif call.data == "click16":
	                key = "-MKkNEFMU5oqtT8duL7W"
			       
	            elif call.data == "click17":
	                key = "-MKkNEFMU5oqtTfkuL7W"
			      
	            elif call.data == "click18":
	                key = "-MKkNEjsU5oqtT8duL7W"
			     
	            elif call.data == "click19":
	                key = "-MKkNQc1BGQVctt93otb"
			     
	            elif call.data == "click20":
	                key = "-MKkNQc1BGQVctcb3otb"
			    
	            elif call.data == "click21":
	                key = "-MKkNQc1ndQVctt93otb"
			     
	            elif call.data == "click22":
	                key = "-MKkO0Ki8fKedZx0vNL4"
			     
	            elif call.data == "click23":
	                key = "-MKkO0KicjKedZx0vNL4"
			     
	            elif call.data == "click24":
	                key = "-MKkO0Ki8fncdZx0vNL4"
			     
	            elif call.data == "click25":
	                key = "-MKkOIxuQjwLsSqtDnw1"
			      
	            elif call.data == "click26":
	                key = "-MKkOIxuQjwLvjqtDnw1"
			    
	            elif call.data == "click27":
	                key = "-MKkOIxuQjwznSqtDnw1"
	            elif call.data == "click 28" :
	                key = ""
			      #  ----------------------------------#
	            bot.send_message(call.message.chat.id, text = "RUN💓💫-- Send URL", parse_mode="markdown")
	            @bot.message_handler(func=lambda m:True)
	            def content(message):
	                d = message.text    
	                bot.send_message(message.chat.id,"* Wait 💥⛈️*", parse_mode="markdown")
					
					#-------------------------Create Data-------------------------#
					
					
	                db.child("bein").child(key).update({"beinlive": d})
	                bot.send_message(message.chat.id,"Done -- ✨💫")
	                print (key+db)
			        #----------------------bein_1---------------------------#
		
	
		
	        #-------------------------- comander_card ------------#
	@bot.message_handler(commands=['card'])
	
	def wel(message): 
	    SE = "2" 
	    h_card = types.InlineKeyboardMarkup()
	    button1 = types.InlineKeyboardButton(text = "Add Card", callback_data= "add")
	    h_card.add(button1)
	    bot.reply_to(message, text="""<strong>💫 Hello Pro : Islam 😇
	💫 Bot El-Joker ViP  
	💫 Ch : @Y_G_U
	💫 Program Bot : Islam El-shenawy 💓
	</strong>  """, reply_markup=h_card, parse_mode="html")
	
	    if SE == "2":
		    @bot.callback_query_handler(func=lambda w: True)
		#----------------------card_2----------------------------#
		
		    def callback_date(w):
		    
			    
			    if w.data == "add":
			        qq = random.randrange(0,999999999)
			    bot.send_message(w.message.chat.id, text = "RUN💓💫-- Send URL", parse_mode="markdown")
			    @bot.message_handler(func=lambda m:True)
			    def content_card(message):
			    	
			        dd = message.text    
			        bot.send_message(message.chat.id,"* Wait 💥⛈️*", parse_mode="markdown")
			#-------------------------------------------------#
			        db.child("card").child(qq).set({"card": dd, "server": dd})
			        bot.send_message(message.chat.id,"Done -- 💫✨")
			#----------------------card2---------------------------#
	
	#-----------------commander Movie-----------------#
	@bot.message_handler(commands=['movie'])
	
	def start(message):
	    SE = "3"
	    h_movie = types.InlineKeyboardMarkup()
	    button1 = types.InlineKeyboardButton(text = "Action", callback_data= "click1")
	    button2 = types.InlineKeyboardButton(text = "Trend", callback_data= "click2")
	    button3 = types.InlineKeyboardButton(text = "Kids", callback_data= "click3")
	    button4 = types.InlineKeyboardButton(text = "New", callback_data= "click4")
	    button5 = types.InlineKeyboardButton(text = "Horror", callback_data= "click5")
	  
	    h_movie.add(button1, button2,button3, button4, button5)
	    bot.reply_to(message, text="""<strong>⌔ Hello Pro :
	⌔ Bot El-Joker ViP 💓💫  
	⌔ Ch : @Y_G_U
	⌔ Program Bot : Islam Elshenawy 💓🌹
	</strong>  """, reply_markup=h_movie, parse_mode="html")
	
	
	    if SE == "3":
	        
		    @bot.callback_query_handler(func=lambda mo: True)
		#----------------------movie_3----------------------------#
		
		    def callback_date(mo):
		
			    
			    time.sleep(1)
			    if mo.data == "click1":
			        page = 0
			        sta = 1
			        seli ="1"
					      
			        bot.send_message(mo.message.chat.id, text = "RUN💓💫-- Action", parse_mode="markdown")
			    elif mo.data == "click2":
			        page = 0
			        sta = 1
			        seli = "2"
				  
			        bot.send_message(call.message.chat.id, text = "RUN💓💫-- Trend", parse_mode="markdown")
			    elif mo.data == "click3":
			        page = 0
			        sta = 1
			        seli = "3"
				  
			        bot.send_message(call.message.chat.id, text = "RUN💓💫-- Kids", parse_mode="markdown")
			    elif mo.data == "click4":
			        page = 0
			        sta = 1
			        seli = "4"
				  
			        bot.send_message(call.message.chat.id, text = "RUN💓💫-- New", parse_mode="markdown")
			    elif mo.data == "click5":
			        page = 0
			        sta = 1
			        seli = "5"
				  
			        
			    	
			       
				#bot = telebot.TeleBot(token)
				#@bot.message_handler(commands=["start"])
				#def welcome(message):
					#bot.send_message(message.chat.id,"RUN💓💫")
			    ioi = 1
			    oio = 1
				#page = 1
				#sta = 1
			    sta2 = 1
			
				
				
				
			    while sta == sta2:
			        if page <= 1:
					
				
				
				        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
				        mainURL_action = "https://one.akwam.cz/movies?section=0&category=18&rating=0&year=0&language=0&formats=0&quality=0"
				        mainURL_trend = "https://one.akwam.cz/movies?section=0&category=72&rating=0&year=0&language=0&formats=0&quality=0"
				        mainURL_kids = "https://one.akwam.cz/movies?section=0&category=88&rating=0&year=0&language=0&formats=0&quality=0"
				        mainURL_top_10 = "https://one.akwam.cz/movies?section=0&category=19&rating=0&year=0&language=0&formats=0&quality=0"
				        mainURL_horror = "https://one.akwam.cz/movies?section=0&category=22&rating=0&year=0&language=0&formats=0&quality=0"
				        headers={
				            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
				        }
					
					
				        page = page+ioi
				        print(f"    page is   ----------------   {page}---------------")
				        bot.send_message(mo.message.chat.id, text = f"RUN💓💫-- page is   ---   {page} ---", parse_mode="markdown")
					
					
					    #seli = "1" input("**- please slelect \n *1-action\n*2-trend\n*3-kids\n*4-top10\n*5-horror\n")
				        if seli=="1":
				            mainURL = f"https://akwam.im/movies?section=0&category=18&rating=0&year=0&language=0&formats=0&quality=0&page={page}"
				            MMM = "action"
				        elif seli=="2":
				            mainURL = f"https://akwam.im/movies?section=0&category=72&rating=0&year=0&language=0&formats=0&quality=0&page={page}"
				            MMM = "trend"
				        elif seli=="3":
				            mainURL = f"https://akwam.im/movies?section=0&category=19&rating=0&year=0&language=0&formats=0&quality=0&page={page}"
				            MMM = "kids_film"
				        elif seli=="4" :
				            mainURL = f"https://akwam.im/movies?section=0&category=19&rating=0&year=0&language=0&formats=0&quality=0&page={page}"
				            MMM = "new_film"
				        elif seli=="5" :
				            mainURL = f"https://akwam.im/movies?section=0&category=22&rating=0&year=0&language=0&formats=0&quality=0&page={page}"
				            MMM = "horror"
					
					    
					    
				        s = requests.Session()
				        r = s.get(mainURL)
				        soup = BeautifulSoup(r.content, "html.parser")
				
				
				        for movie in soup.findAll('div', {'class':'entry-image'}):
				            iii = 1
				            pop = 1
				            one = 1
				            value_fire = "0123456789"
				            qq =random.randrange(0,999999999)
				        
				            value_fire2 = 'Islam-Joker-ViP'
				            movielink = movie.find('a')
				            link = movielink['href']
				            
				
				            name = link.split("https://akwam.im/movie")[1][+6:]
				            print(name)
				        
				            req = requests.Session()
				            req2 = req.get(link)
				            soup2 = BeautifulSoup(req2.content, "html.parser")
				            for img in soup2.findAll('div', {'class':'col-lg-3 col-md-4 text-center mb-5 mb-md-0'}):
				            
				                aa = img.find('a')
				                k = aa['href']
				                
				        
				                for inf in soup2.findAll('div', {'class':'font-size-16 text-white mt-2'}):
				                    inf_find = inf.find('span')
				                
				                    if pop==1:
				                        inf_pop1 = inf_find
				                        pop = pop+one
				                    
				                    elif pop==2:
				                        inf_pop2 = inf_find
				                        pop = pop+one
				                    
				                    elif pop==3:
				                        inf_pop3 = inf_find
				                        pop = pop+one
				                    
				                    elif pop==4:
				                        inf_pop4 = inf_find
				                        pop = pop+one
				                    
				                    elif pop==5:
				                        inf_pop5 = inf_find
				                        pop = pop+one
				                    
				                    elif pop==6:
				                        inf_pop6 = inf_find
				                        pop = pop+one
				                        break
				                
				            
				            
				                for down in soup2.findAll('div', {'class':'col-lg-6 col'}):
				                    aa2 = down.find('a')
				                    k2 = aa2['href']
				                
				                    if iii==1:
				                        down2 = s.get(k2)
				                        down_m = BeautifulSoup(down2.content, "html.parser")
				                        for download in down_m.findAll('div', {'class':'content'}):
				                            dow22 = download.find('a')
				                            kb = dow22['href']
				                        
				                        
				                            down_f = s.get(kb)
				                            down_final = BeautifulSoup(down_f.content, "html.parser")
				                        
				                            for download_final in down_final.findAll('div', {'class':'btn-loader'}):
				                                dow5 = download_final.find('a')
				                                kb_link = dow5['href']
				                                
				                                iii = one+1
				                    else:
				                        ccccc = "7"
				                        
				            
				                        
				                        
				                    
				
				
				
				                inform_pop ={
				                    inf_pop1,
				                    inf_pop2,
				                    inf_pop3,
				                    inf_pop4,
				                    inf_pop5,
				                    inf_pop6
				                
				                };
				            
				            # Config/Setup
				            #-------------------------------------------------------------------------------
				                firebaseConfig = {
				                    "apiKey": "AIzaSyCZaGvjUlz_fzBpcqG7AGHMhT6zXl7zHF0",
				                    "authDomain": "startv2-2a68a.firebaseapp.com",
				                    "projectId": "startv2-2a68a",
				                    "databaseURL": "https://startv2-2a68a.firebaseio.com",
				                    "storageBucket": "startv2-2a68a.appspot.com",
				                    "messagingSenderId": "743024432763",
				                    "appId": "1:743024432763:web:da4e5680d9c6c9961af4de",
				                    "measurementId": "G-KEJ980W0HS"
				                };
				                firebase = pyrebase.initialize_app(firebaseConfig)
				                db = firebase.database()
				
				                data = {"image": k, "Name": name, "url1": kb_link}
				            #-------------------------------------------------------------------------------
				            # Create Data
				
				
				                db.child(MMM).child(name).set(data) 
				                db.child("movie").child(name).set(data)  
				
			                 
			        else:
			        	print ("Done💫💓")
			        #----------------------movie_3----------------------------#
	
	#--------------------------upgrade_ViP----------------------#
	@bot.message_handler(commands=['user'])
	
	    
	def user(message):  
	    SE = "4" 
	    h_user = types.InlineKeyboardMarkup()
	    button1_user = types.InlineKeyboardButton(text = "Free🙁", callback_data= "add_u")
	    button2 = types.InlineKeyboardButton(text = "ViP💫", callback_data= "add_q")
	    h_user.add(button1_user,button2)
	    bot.reply_to(message, text="""<strong>💫 Hello Pro : Islam 😇
	💫 Bot El-Joker ViP  
	💫 Ch : @Y_G_U
	💫 Program Bot : Islam El-shenawy 💓
	</strong>  """, reply_markup=h_user, parse_mode="html")
	
	
	    if SE == "4":
		    print ("-----4-----")
		    
		#------------------------user_4--------------------#
		    @bot.callback_query_handler(func=lambda az: True)
		    def callback_date(az):
		    
		        if az.data == "add_u":
			        qq = "free"
			        ok = "Successful Update Free💦"
		        elif az.data == "add_q":
			        qq = "vip"
			        ok = "Successful Update VIP✨💫"
		        bot.send_message(az.message.chat.id, text = "RUN💓💫-- Send uid", parse_mode="markdown")
		        @bot.message_handler(func=lambda m:True)
		        def content_user(message):
			    	
		            uid = message.text    
		            bot.send_message(message.chat.id,"* Wait 💥💓*", parse_mode="markdown")
			#-------------------------------------------------#
		            db.child("account").child(uid).update({"statue": qq})
		            bot.send_message(message.chat.id,ok)
		
			 
			#----------------------user4----------------------------#
	#--------------------------Restart----------------------#
	@bot.message_handler(commands=['restart'])
	
	    
	def user(message):  
	    SE = "5" 
	    print (SE+1)
	    h_user = types.InlineKeyboardMarkup()
	    button1_user = types.InlineKeyboardButton(text = "Free🙁", callback_data= "add_u")
	    button2 = types.InlineKeyboardButton(text = "ViP💫", callback_data= "add_q")
	    h_user.add(button1_user,button2)
	    bot.reply_to(message, text="""<strong>💫 Hello Pro : Islam 😇
	💫 Bot El-Joker ViP  
	💫 Ch : @Y_G_U
	💫 Program Bot : Islam El-shenawy 💓
	</strong>  """, reply_markup=h_user, parse_mode="html")
	
	
	    if SE == "5":
		    print ("-----5-----")
		    
		#------------------------user_4--------------------#
		    @bot.callback_query_handler(func=lambda az: True)
		    def callback_date(az):
		    
		        if az.data == "add_u":
			        qq = "free"
			        ok = "Successful Update Free💦"
		        elif az.data == "add_q":
			        qq = "vip"
			        ok = "Successful Update VIP✨💫"
		        bot.send_message(az.message.chat.id, text = "RUN💓💫-- Send uid", parse_mode="markdown")
		        @bot.message_handler(func=lambda m:True)
		        def content_user(message):
			    	
		            uid = message.text    
		            bot.send_message(message.chat.id,"* Wait 💥💓*", parse_mode="markdown")
			#-------------------------------------------------#
		            db.child("account").child(uid).update({"statue": qq})
		            bot.send_message(message.chat.id,ok)
		
			 
			#----------------------Restart----------------------------#
	#--------------------------Restart----------------------#
	@bot.message_handler(commands=['chat'])
	
	    
	def user(message):  
	    SE = "6" 
	    
	    h_user = types.InlineKeyboardMarkup()
	    button1_user = types.InlineKeyboardButton(text = "Open", callback_data= "add_u")
	    button2 = types.InlineKeyboardButton(text = "Close", callback_data= "add_q")
	    h_user.add(button1_user,button2)
	    bot.reply_to(message, text="""<strong>💫 Hello Pro : Islam 😇
	💫 Bot El-Joker ViP  
	💫 Ch : @Y_G_U
	💫 Program Bot : Islam El-shenawy 💓
	</strong>  """, reply_markup=h_user, parse_mode="html")
	
	
	    if SE == "6":
		    print ("-----5-----")
		    
		#------------------------user_4--------------------#
		    @bot.callback_query_handler(func=lambda az: True)
		    def callback_date(az):
		    
		        if az.data == "add_u":
			        qq = "open"
			        ok = "Successful open chat💦"
		        elif az.data == "add_q":
			        qq = "close"
			        ok = "Successful close chat💦"
		        bot.send_message(az.message.chat.id, text = "RUN💓💫-- Are you sure ??!", parse_mode="markdown")
		        @bot.message_handler(func=lambda m:True)
		        def content_user(message):
			    	
		            uid = message.text    
		            bot.send_message(message.chat.id,"* Wait 💥💓*", parse_mode="markdown")
			#-------------------------------------------------#
		            db.child("chat_open").child("-N1Vn_HuKFiozQ2wzJ0W").update({"oc": qq})
		            bot.send_message(message.chat.id,ok)
		            print(qq+db)
		
			 
			#----------------------user4----------------------------#
	bot.polling()
	time.sleep(.01)
except:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_bot}&text=Successful restarted✨💦')
    restart()
    
		        
	