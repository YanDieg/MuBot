# MuBot
## The Official MuHack's Telegram bot (@muhackbot)
Developed by [Yanez Diego Parolin](https://yanezdiegoparolin.it)

### Index
- [About the Bot](#about-the-bot)
  - [Developer](#developer)
  - [How is made](#how-is-made)
  - [Why was made](#why-is-made)
- [Guide](#guide)
  - [Precondition](#precondition)
    - [Create a bot](#create-a-bot)
    - [Get Google API](#get-google-api)
      - [Google Drive](#google-drive)
      - [Google Sheet](#google-sheet)
    - [Host](#host)
      - [PythonAnywhere](#pythonanywhere)
  - [Setup](#setup)
    - [Explanation of the code](#explanation-of-the-code)
      - [Library](#library)
      - [Google API implementation](#google-api-implementation)
      - [Emoji use](#emoji-use)
      - [Other](#other)
    - [Add new command](#add-new-command)
      - [Add new message](#add-new-message)
      - [Add new keyboard menu](#add-new-keyboard-menu)
      - [Add new raw command](#add-new-raw-command)
      - [Add admin command](#add-admin-command)
    - [Edit message structure](#edit-message-structure)
    - [Use emoji](#use-emoji)
    - [Use markdown](#use-markdown)
  - [Other guide](#other-guide)
  
# About the bot
MuBot is the official MuHack's Telegram bot. Muhack is an hackerspace and an university's association (more info [here](https://muhack.org). 
It has been developed by YanDieg, using Python (and its library).
## Developer
[Yanez Diego Parolin](https://yanezdiegoparolin.it), alias YanDieg, is a student of Computer Engineering at University of Brescia. You can contact him on Telegram [@YanDieg](https://t.me/yandieg).
His personal website is available [here](https://yanezdiegoparolin.it).
## How is made
This bot is based on Python. It uses the library [python-bot-telegram](https://python-telegram-bot.org/) for Telegram API and it is hosted on [PythonAnywhere](https://www.pythonanywhere.com/).
It also uses an optional library, called [Emoji](https://pypi.org/project/emoji/) to decorate it.
## Why is made
MuHack needed a "organizer" to show to associates and external people the projects, the events, the tasks and its info, so the boards chose to develop a Telegram Bot.
# Guide
This guide is useful if you want to develop a Telegram bot for your association, organization, school, group ... 
Other simple guide will be available in italian on MuHack's website and in english on YanDieg's website. 
## Precondition
Before proceeding with the setup, you need these things:
1) Telegram Bot
2) Active Google API (Optional - only if you want to read/write google documents)
3) Have a place where host the bot
### Create a bot
1) Start a Telegram chat with [@BotFather](https:t.me/BotFather)
2) Use the /newbot command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.
3) *Save this token* - you will need it for the "Setup phase"
You can "personalize" your bot with other commands. [Click Here](https://core.telegram.org/bots#creating-a-new-bot) for further information.
### Get Google API
This is optional! If you don't want to integrate your bot with Google, go to the next [step](#host)
#### Google Drive
Follow this guide to enable "Drive API" -> [GUIDE](https://gspread.readthedocs.io/en/latest/oauth2.html)
#### Google Sheet
As before but for "Sheet API"
### Host
You need to host your bot on server, because it will be running continuously. I suggest to use PythonAnywhere service ... IT IS FREE!
#### PythonAnywhere
[PythonAnywhere](https://www.pythonanywhere.com/) is a service that allows you to host, run and code Python in the cloud.
The dev chose it because it is free (there is a free plan, it is enough to host your Telegram Bot), safe and handy.
Create a new account, and let start with [Setup steps](#setup)!
## Setup
In this section you will go to analyze the code of this bot. You will see how to modify it and adapt it to your needs.
### Explanation of the code
It is the most difficult explanation ...
I put it in a guide. [Click here](/manual/guide.md) to read it or go to the directory "manual" and open the file "guide.md"
#### Library
#### Google API implementation
#### Emoji Use
#### Other
### Add new command
#### Add new message
#### Add new keyboard menu
#### Add new raw command
#### Add admin command
### Edit message structure
### Use Emoji
### Use markdown
## Other Guide

  
