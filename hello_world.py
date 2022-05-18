from flask import Flask
from random import choice
#Create our base app
app = Flask(__name__)

#Route to the default page
@app.route('/', methods=['GET'])
def homepage():
    things_to_say = ['Shalom.',
                     'Welcome friend!',
                     ':)',
                     ':D',
                     ';D',
                     ':*',
                     ';)',
                     'Eh, What?',
                     'Hello world!',
                     'If you made it here...you survived! Congrats.',
                     "'I' before 'E', except after 'C' or sounding in 'EIGH', as in 'Neighbor' and 'Weigh.'",
                     "What are you going to do yesterday?",
                     "Just realized I'm copying Minecraft's MOTD' scheme RIP. (Don't sue me plz D:)",
                     "2+2 = FISH.",
                     "You have beautiful eyes O.O",
                     "I wana steal",
                     "Nothing matters...wait...nothing matters!",
                     "Ta-ta-ke.",
                     "Meow.",
                     "Woof.",
                     "Mew.",
                     "Bork."
                     "8)",
                     "I should really be in bed RN.",
                     "Shoutout to my grandpa for a kick-ass last name!",
                     "I just want to own a home.",
                     "Blue Moon is a perfectly valid currency, as far as I'm concerned.",
                     "CooCoo...who would want to buy a CooCoo?",
                     "I think it's time YOU had a pink cloud summer...",
                     "These emails cost $6 a month!"
                     ]
    return("Here's your super special message:\n\r\n\r"+choice(things_to_say)+'\n\n\n\n And now...Here is the Kate section! Woo! :o')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
