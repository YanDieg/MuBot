from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ParseMode
from emoji import emojize

# manage admin
import os
import sys
from threading import Thread

# start google drive
import gspread
from oauth2client.service_account import ServiceAccountCredentials
SCOPES = ["https://www.googleapis.com/auth/drive"]
# This is the PATH for your Service Account Credentials of Google Drive (See Guide)
PATH = os.getcwd() + "/credential/googleapi.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(PATH, SCOPES)
connection = gspread.authorize(credentials)

worksheet_con = None
ws_projects = None
ws_events = None
ws_tasks = None
list_projects = None
list_events = None
list_tasks = None
# end google drive

# file
text_about_us = None
text_about_the_bot = None
text_help = None
	

# message
START_MESSAGE = "Your start message"
UNKNOWN_MESSAGE ="Your unknown error message"
MENU_MESSAGE = "Your message to show menu option"

# start optional emoji
# If you don't use emoji in this message, you can remove this part (if you leave it, there won't problem. It will be unnecessary)
START_MESSAGE = emojize(START_MESSAGE, use_aliases=True)
UNKNOWN_MESSAGE = emojize(UNKNOWN_MESSAGE, use_aliases=True)
MENU_MESSAGE = emojize(MENU_MESSAGE, use_aliases=True)
# end optional emoji

# Bot token (see Guide)
token = "yourToken"

# start menu building
# create command and text command
PROJECTS_COMMAND = "Project"
EVENTS_COMMAND = "Events"
HELP_US_COMMAND ="Help us"
INFO_COMMAND = "Info"

# start optional emoji
# If you don't use emoji in this message, you can remove this part (if you leave it, there won't problem. It will be unnecessary)
PROJECTS_COMMAND = emojize(PROJECTS_COMMAND, use_aliases=True)
EVENTS_COMMAND = emojize(EVENTS_COMMAND, use_aliases=True)
HELP_US_COMMAND = emojize(HELP_US_COMMAND, use_aliases=True)
INFO_COMMAND = emojize(INFO_COMMAND, use_aliases=True)
# end optional emoji

# menu-keyboard command layout (see Guide)
custom_keyboard = [[PROJECTS_COMMAND, EVENTS_COMMAND], [HELP_US_COMMAND, INFO_COMMAND]]
markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
# end menu building

#BOT /commands
def bot_start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=START_MESSAGE, reply_markup=markup)

def bot_see_menu(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=MENU_MESSAGE, reply_markup=markup)

def bot_about_bot(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_about_the_bot, parse_mode=ParseMode.MARKDOWN)

def bot_help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_help, parse_mode=ParseMode.MARKDOWN)

#BOT inner-function
def bot_projects(bot, update):
    # start building message struct
    project_text_msg = "*Project at MuHack* \n"
    project_text_msg += "_For futher information please check project's page or our_ [website](https://muhack.org)\n\n"
    for l in list_projects
        #PROJECT NAME
        project_text_msg += "*" + l[0] + "*" + "\n"
	   #DESC
        project_text_msg += "_" + l[1] + "_" + "\n"
        #DEV NAME
        project_text_msg += "Dev: " + l[2] + "\n"
        #PROJECT's PAGE
        project_text_msg += "Project's page: " + "[" + l[3] + "]" + "\n\n"
    # stop building message struct
    bot.send_message(chat_id=update.message.chat_id, text=project_text_msg, parse_mode=ParseMode.MARKDOWN)

def bot_helpus(bot, update):
    # start building message struct
    helpus_text_msg = "*Tasks* \n"
    helpus_text_msg += "for futher information about the tasks or to help contact @yandieg or @ceres\_c\n\n"
    for l in list_tasks:
        #TASK
        helpus_text_msg += "*" + l[0] + "*" + "\n"
	   #TASK DESC
        helpus_text_msg += "_" + l[1] + "_" + "\n\n"
    # stop building message struct
    bot.send_message(chat_id=update.message.chat_id, text=helpus_text_msg, parse_mode=ParseMode.MARKDOWN)

def bot_events(bot, update):
    # start building message struct
    event_text_msg = "*MuHack's Events* \n"
    event_text_msg += "_For futher information please check event's page or our_ [website](https://muhack.org/events)\n\n"
    for l in list_events:
	   #EVENT NAME
        event_text_msg += "*" + l[0] + "*" + "\n"
	   #EVENT WHEN
        event_text_msg += "`When?` " + l[1] + "\n"
        #EVENT WHERE
        event_text_msg += "`Where?` " + l[2]  + "\n"
	   #EVENT DESC
        event_text_msg += "_" + l[3] + "_\n"
        event_text_msg += "Event's page: [" + l[4] + "]" + "\n\n"
    # stop building message struct
    bot.send_message(chat_id=update.message.chat_id, text=event_text_msg, parse_mode=ParseMode.MARKDOWN)

def bot_info(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_about_us, parse_mode=ParseMode.MARKDOWN)

#Bot Error-Unknown message
def bot_unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=UNKNOWN_MESSAGE, parse_mode=ParseMode.MARKDOWN)

#BOT Menu Option (ReplyKeyboardMarkup)
def menu(bot, update):
    if update.message.text == PROJECTS_COMMAND:
        bot_projects(bot, update)
    elif update.message.text == EVENTS_COMMAND:
        bot_events(bot, update)
    elif update.message.text == HELP_US_COMMAND:
        bot_helpus(bot, update)
    elif update.message.text == INFO_COMMAND:
        bot_info(bot, update)
    else:
        bot_unknown(bot, update)

# get data from google sheet and save it
def getDataGoogle():
    global worksheet_con, ws_projects, ws_events, ws_tasks, list_projects, list_events, list_tasks
    worksheet_con = connection.open("MuHack")
    ws_projects = worksheet_con.worksheet("projects")
    ws_events = worksheet_con.worksheet("events")
    ws_tasks = worksheet_con.worksheet("tasks")
    list_projects = ws_projects.get_all_values()
    list_events = ws_events.get_all_values()
    list_tasks = ws_tasks.get_all_values()

# get data from text file
def getTextFromFile():
	global text_about_the_bot, text_about_us, text_help
	PATH_ABOUT_US = os.getcwd() + "/text/about_us.txt"
	PATH_ABOUT_BOT = os.getcwd() + "/text/about_bot.txt"
	PATH_HELP = os.getcwd() + "/text/help_guide.txt"
	with open(PATH_ABOUT_US, 'r') as f:
		text_about_us = f.read();
	with open(PATH_ABOUT_BOT, 'r') as f:
		text_about_the_bot = f.read();
	with open(PATH_HELP, 'r') as f:
		text_help = f.read();

# Update the data from google sheet
def updateAPI():
    connection.login()
    getDataGoogle()

def callback_APIgoogle(bot, job):
    updateAPI()


#Funzionamento del BOT
def main():
    # Init BOT
    updater = Updater(token)
    dispatcher = updater.dispatcher
    job = updater.job_queue
    
    getDataGoogle()
    getTextFromFile()

    #UPDATE DATA EVERY 3 HOURS
    repeat = 10800
    job.run_repeating(callback_APIgoogle,interval=repeat, first=0)
    
    # Function to restart bot only for Filter.user = admin
    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()
        update.message.reply_text(' Bot has been updated!')

    dispatcher.add_handler(CommandHandler('restart', restart, filters=Filters.user(username='@YanDieg')))
    dispatcher.add_handler(CommandHandler('updateAPI', callback_APIgoogle, filters=Filters.user(username='@YanDieg')))

    # Add command
    start_handler = CommandHandler('start', bot_start)
    reset_handler = CommandHandler('menu', bot_see_menu)
    about_handler = CommandHandler('about_bot', bot_about_bot)
    help_handler = CommandHandler('help', bot_help)
    
    # Add command declared before (like project, events ...)
    menu_handler = MessageHandler(Filters.text, menu)
    
    # Add unknow error IT MUST TO BE THE LAST
    unknown_handler = MessageHandler(Filters.command, bot_unknown)

    # Add command handler
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(reset_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(menu_handler)
    dispatcher.add_handler(unknown_handler)

    #loop
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
