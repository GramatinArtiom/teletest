import random
from telebot import TeleBot

bot = TeleBot("6205638174:AAFFedDJeZ50JkRq6UgNwXK8zAerjMtnMeA")
sadcommandslist = ['depression', 'sad', 'hardtime', 'depressive']
happycommandlist = ['happy', 'glad', 'goodmood']
motivationalcommandlist = ['motivation', 'gym', 'sport', 'motivational']
bestcommandlist = ['popular', 'hits', 'best', 'recommended']
commandlist = [sadcommandslist, happycommandlist, motivationalcommandlist, bestcommandlist]

sadmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1?si=e3d9b4d2fe284840',
                'https://open.spotify.com/playlist/53x5zb5JQlXJ9wBR3iImDL?si=ca4ee553e3044b3d',
                'https://open.spotify.com/playlist/2LDCn6vNamfbM4Rc6V3Yh3?si=1844deda9df74dff',
                'https://open.spotify.com/playlist/7rKMzvTmF9qApvtgd6Rzmd?si=6e2392dc430d4620',
                'https://open.spotify.com/playlist/3Ar6l24242VBGny7S9VxcD?si=6bcfecdd2cec4b11']
happymusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=9f7d0254e4204789',
                  'https://open.spotify.com/playlist/37i9dQZF1DWZKuerrwoAGz?si=39e35d30923c40e4',
                  'https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2?si=33d1932eedd64e27',
                  'https://open.spotify.com/playlist/37i9dQZF1DWSf2RDTDayIx?si=01191d6ebb5b4175',
                  'https://open.spotify.com/playlist/4AnAUkQNrLKlJCInZGSXRO?si=228df917906a494f']
motivationmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy?si=cf92780a36d64702',
                       'https://open.spotify.com/playlist/6o7IK7K9wanDCWTlWFWqj9?si=04c599cfdff44038',
                       'https://open.spotify.com/playlist/1Oe9RGsTp7XGCcY91EgKtx?si=5c13487bf8344bbc',
                       'https://open.spotify.com/playlist/4077gmwIYxf3EsBwowfDmZ?si=aae1e445042145e8',
                       'https://open.spotify.com/playlist/78Suoigk80gI9mI9z5tYl8?si=83c88259f8ee4a31']
bestmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=12642ab496cd41e5',
                 'https://open.spotify.com/playlist/31ymdYCITDnZRtkKzP3Itp?si=5f81c6096a1d4bf8',
                 'https://open.spotify.com/playlist/0cc8YMQWsSzODyTpdVB6mI?si=a59e217e738042f3',
                 'https://open.spotify.com/playlist/6ZTpgxK6BT92mmsqwETj9l?si=7126d2291b344d82',
                 'https://open.spotify.com/playlist/37i9dQZF1DWSvKsRPPnv5o?si=ef4f344a313c441c']
jazzmusiclist = ['https://open.spotify.com/album/6Zrv82YKWMG1BuwkVCD3vU?si=O8O5R-F9RYaWmffPnhfKNw'
                 'https://open.spotify.com/playlist/35i05dxUnfnU0ulnimZh3V?si=9f0c01a1aa8a4fb9'
                 'https://open.spotify.com/playlist/05Hd48jdQIz3s8WRrvGnzf?si=957c32353bcb4688']
hiphopmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DWUFmyho2wkQU?si=e2d71e62539f4227'
                   'https://open.spotify.com/playlist/6p3IRyXLrl28mu33AHtqnj?si=61148e46c6f447e4'
                   'https://open.spotify.com/playlist/37i9dQZF1DX48TTZL62Yht?si=f8e16d6aa1894640']
rockmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U?si=744b475ea5bc426b'
                 'https://open.spotify.com/playlist/3qu74M0PqlkSV76f98aqTd?si=9778878e0cb943ca'
                 'https://open.spotify.com/playlist/37i9dQZF1DX8FwnYE6PRvL?si=a87219791eb74639']
classicalmusiclist = ['https://open.spotify.com/playlist/62n7TtrAWY1BeNg54yigFe?si=2c0c351aa0884688'
                      'https://open.spotify.com/playlist/1h0CEZCm6IbFTbxThn6Xcs?si=3331e6f2dbbd4f34'
                      'https://open.spotify.com/playlist/5E4CbUOCiUXw2Fh8Foq51V?si=18f8c25f3e984f42']
popmusiclist = ['https://open.spotify.com/playlist/37i9dQZF1DX1H4LbvY4OJi?si=043f7761b06545cc'
                'https://open.spotify.com/playlist/3ZgmfR6lsnCwdffZUan8EA?si=395a1318009c4baa'
                'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=4869ca804a7e4bb6']


@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Hello, {message.from_user.first_name} {message.from_user.last_name}! I am a bot that was "
                     f"created to find some spotify playlists for you ! I"
                     "really hope that I will help you! \nTo find playlists, just type a word that describes a "
                     "playlist with which type of music you want,"
                     " Example: depression , sad , \n"
                     "happy , motivational , gym , best, jazz, rock, hiphop, pop, classical.")


@bot.message_handler()
def main(message):
    if message.text.lower() in sadcommandslist:
        song = random.choice(sadmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() in happycommandlist:
        song = random.choice(happymusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() in motivationalcommandlist:
        song = random.choice(motivationmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() in bestcommandlist:
        song = random.choice(bestmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() == 'jazz':
        song = random.choice(jazzmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() == 'hip-hop' or message.text.lower() == 'hiphop' or message.text.lower() == 'hip hop':
        song = random.choice(hiphopmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() == 'rock':
        song = random.choice(rockmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() == 'classical':
        song = random.choice(classicalmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    elif message.text.lower() == 'pop':
        song = random.choice(popmusiclist)
        bot.send_message(message.chat.id, "Sure! That's what I found!\n" + str(song) + "&nd=1")
    else:
        bot.send_message(message.chat.id, "I think I can't help you with this, try another word!")


bot.polling(none_stop=True)
