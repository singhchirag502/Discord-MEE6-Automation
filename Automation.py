from pynput.mouse import Button,Controller
mouse=Controller()
import time
from pynput.keyboard import Key, Controller
keyboard=Controller()
'''
#l=['Maybe our team will get your some liverage','Because you gys are soo ','inactive','You knw wt guys ??','Only last 2 days of workshop is left.','All I know is that, we are gonna end up forminga Madian Family and memory that we will never forget.','Its for the first time , I am connected to so many people across the whole nation.','Were gonna call this as MAD family']
l=["Day 0 is into..we learned bout internet and how it works",
"Day 1 is when we setup our Django environment"," and created WebApp and flipkart",
"Day 2: we leanred about the flow in django ","and later we created a sime feed back form",
"creating a model>make migrations>migrate> creating a form in forms.py> views > html",
"Then setting up the url so thaf when we give /feedback we end up in that page",
"Day 3 : We created a Product information table using models",
"Forms was not needed here",
"But we have to register that"," model in admin.py to enter it into database",
"We created a url and wrote a funtion in our views",
"We learned about GET and POST",
"Now based on that we wrote a variable based url",
"Next we used bootstrap ","to get an example nav bar and home page",
"Then we used a simple tabke fetched from bootstrap",
"to contain the data of products in various categories",
"We wrote the function for it as well",
"To fetch the data based on categories",
"We meabed about the difference between url and path",
"We thenearndd about orm statements",
"That was the 1st Chunk of back end",
"Then we stepped into the world of front end",
"We setup an environment first",
"Vs code and all",
"in frontend we started from basic html ","to form to tables to CSS",
"We learned about different elements in html",
"and then in css from very basic we started",
"what is height width position display property and its values",
"the most imp part of html is div / span tags and class and ids",
"We did CSS positions like static , abstract , Absolute and Fixed .",
"those are the values we have for properties",
"we saw how we can link css files externally",
"We will be getting a 5 day break after the session where can re watcj the session."]
'''
l=[" play senorita","!play senorita",
   " play perfect","!play perfect",
   " play closer","!play closer",
   " play galway girl","!play senorita",
   " play i dont care","!play i dont care",
   " play havana","!play havana",
   " play liar","!play liar",
   " play shape of you","!play shape of you",
   " play something just like this","!play something just like this",
   " play blank space","!play blank space",
   " play love story","!play love story",
   " play bad blood","!play bad blood",
   " play delicate","!play delicate",
   " play first man","!play first man",
   " play lover","!play lover",
   " play a thousand years","!play a thousand years",
   " play photgraph","!play photgraph",
   " play attention","!play attention",
   " play changes ","!play changes",
   " play baby","!play baby",
   " play faded","!play faded",
   " play alone","!play alone",
   " play hate u","!play hate u",]
   
   
time.sleep(7)
for i in range(len(l)-1):
    '''
    mouse.position =(954,627)
    time.sleep(1)
    mouse.position = (1078, 590)
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position = (943, 689)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    '''
    keyboard.type(l[i])
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(60)
    
    keyboard.type("skip")
    time.sleep(60)
    keyboard.type("!skip")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    
    keyboard.type(l[i+1])
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(60)
print("FINISHED")
