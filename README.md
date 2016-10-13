# Zahn Center Hackathon Starter Kit

Welcome to the *Zahn Center* Hackathon. This starter kit is intended to introduce you to same frameworks that might be helpful for you in order to solve your problem. Obviously, I won't be able to cover the full usage of each package and thus next to each package or framework name, you will find a link to the project website and a link to the documentation. 

This repository contains 3 sub directories, each one has a description and some examples of the tools that might be useful to solve this particular problem. 

Note that all the packages in this starter kit are only a suggestion and you are not restricted to them only. Feel free to use whatever will help you.

Good luck,

Liron Shimrony


**Note**: The scripts and examples provided here were tested on a VM running **Ubuntu 16.04.1 32 bit** however they suppose to work on any Debian distribution.

#General Notes -- Getting Started

## Development Environment
It is important to have a stable development environment in order to use the development tools efficiently. My recommendation is to work with MacOS or any Debian distribution of Linux (eg. Ubuntu). If you are working under Microsoft Windows, I recommend you to download [VirtualBox](https://www.virtualbox.org) and the latest version of [Ubuntu](https://www.ubuntu.com/download/desktop) before starting any development.
If you are working with Linux, you have the Aptitude package manager (apt-get) installed. In case you are working with a Mac, I would recommend you to install [HomeBrew](http://brew.sh). That way you want need to manually download and install each piece of software.

## Installing PIP
[PIP](https://pip.pypa.io/en/stable/) is a python package manager that will allow us to install different packages quickly. If you don't have it installed on you machine already, you can open shell and install it by running
```bash
sudo pip install python-pip
```
Mac users already have PIP pre-installed. 

## Create a Virtual Environment
In order to isolate our environment, we will install [VirtualEnv](https://virtualenv.pypa.io/en/stable/). This will promise that all the packages for your projects are isolated from the rest of the packages you already installed on your machine. You can install it by running `sudo pip install virtualenv` in your shell.

### Create Your Development Environment
After we installed VirtualEnv, navigate to your working directory (really doesn't matter which one you choose) and run the following command:
```bash
virtualenv [env_name] --no-site-packages
```

Of course, replace `env_name` with the name you want to give your environment. For example: `virtualenv zahnHackathon --no-site-packages`.

After the environment is created, we need to activate it by running:
```bash
source /path/to/env/bin/activate
```

If you created your environment on your desktop, it will be something like 
```bash
source ~/Desktop/zahnHackathon/bin/activate
```

Notice that your command prompt now displays the environment name.
In order to deactivate the environment just run `deactivate`

## Install a Database
For all the problems that you can choose from, a database is an essential part of the solution. My examples will use (MySQL)[https://www.mysql.com] but everything will work the same if you decide to use other flavors of SQL (PostgreSQL, SQLite, etc.)

#### Installation
- **Linux**- `sudo apt-get install mysql-server`
- **Mac**- `brew install mysql`

During the installation process you will need to type a password for MySQL root user

#### Create Users and Databases
After installing MySQL we need to create users so we can use the database. First, launch MySQL as the root user:
```bash
mysql -u root -p
```

After typing your password, create a new user:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost'
FLUSH PRIVILEGES;
exit
```
Where you should replace `username` and `password` with your desired values.

#### Test Your Database
To see that everything is working, run the following from your shell
```bash
mysql -u username -p
```

After typing your password you should be in the Mysql shell.

#### Communicating with Python
In order to user MySQL in python, you must run the following from your shell
```bash
# This will install the tools the build the next packages (linux users only)
sudo apt-get install libmysqlclient-dev

# Install the mysql python adapter
pip install mysql-python
```


## What's Next
After setting up your environment, it is time to start tackle the problem you chose. Just navigate to one of the subdirectories and check out examples that are more specific to your problem.



# Natural Language Processing Kit (NLTK)

## Installation
[NLTK](http://www.nltk.org) can be install using `pip` by running
```bash
pip install nltk
```

NLTK has an extensive amount of information that is not needed by all users. From that reason, after installing it, you will need to choose which sub packages to install.
Run you python shell and execute the following commands
```python
import nltk
nltk.download()
```

For Linux users, it will start the NLTK shell where you need to follow the instructions and download the packages. You can copy and paste the packages identifier from the list below.

For Mac users, this command will open the following window:
![NLTK Menu](nltk.png)
Just choose your desired packages

The following list contains recommended packages:
- Corpora
    + brown
    + twitter_samples
- Models
    + averaged_perceptron_tagger (Parts Of Speech tagging)
    + punkt (Words tokenizer)
    + tagsets (Help on tagsets)
    + universal_tagset (Parts Of Speech tagging)


## Using NLTK
This starter kit is way too short to describe all the capebilities of NLTK. You can read more about it on their [website](http://www.nltk.org). Here is a short example of a very basic usage.

When parsing a sentence, it is important to understand what are the verbs, nouns, adjectives, etc. Doing so, we can actually understand what the user is asking.

The first think we should do with a text input is to strip it from all the punctuation and tokenize it (just create a list of words). After doing that, we can start finding the POS (parts of speech).
You can find the full list of POS by running the following command
```python
import nltk
nltk.help.upenn_tagset()
```

This will output a list with the POS and some examples.

#### Examples
```python
import nltk
from nltk import word_tokenize, pos_tag
import string

# Get all the English alphabet letters and a space
valid_letters = string.letters + ' '
#############
# Example 1 #
#############

text = "Hello, how are you?"

# Remove all punctuation
stripped_text = ''.join([char if char in valid_letters else '' for char in text])

# Tokenize
tokens = word_tokenize(stripped_text)

# Get POS
tags = pos_tag(tokens)

'''
If you print the tags variable you will get the following output

[('Hello', 'NNP'), ('how', 'WRB'), ('are', 'VBP'), ('you', 'PRP')]
NNP = singular proper noun
WRB = WH adverb
VBP = verb, present tense, not 3rd person singular
PRP = pronoun, personal
'''


#############
# Example 2 #
#############

# We do the same process as before
text = "What is the value of Apple stock?"
stripped_text = ''.join([char if char in valid_letters else '' for char in text])
tokens = word_tokenize(stripped_text)
tags = pos_tag(tokens)

'''
If we print the tags variable:
[('What', 'WP'),
 ('is', 'VBZ'),
 ('the', 'DT'),
 ('value', 'NN'),
 ('of', 'IN'),
 ('Apple', 'NNP'),
 ('stock', 'NN')]
 '''
```

 The sentence in the second example has a bit more meaning than the previous one. We can see that we have 3 nouns: Apple (capitalize which might imply a proper noun ), value and stock. 
 Finding POS that way helps us to find the actual question and ignore any noise. The question *What is the value of Apple stock?* can be asked in different ways (when dealing with search engines):
 - Apple stock value
 - How much cost Apple stock
 - What is the price of Apple stock

The common thing for all the questions above are the words Apple and stock, which NLTK gave us without a lot of work.



# ChatBot
[ChatterBot](http://chatterbot.readthedocs.io/en/stable/index.html) is a chatbot package written in python. It has capabilities of integrating with SQL and NoSQL databases and it's quite easy to use.

## Installation
```
pip install chatterbot
```


To create a basic bot:
```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chat bot called MegaBot
bot = ChatBot('MegaBot')

# Train the bot with some basic English
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')

# Let's give it a shot
res = bot.get_response('Good Morning!')
print res
# OUTPUT: I am doing well, how about you?


# Let's try something else
res = bot.get_response('Hello')
print res
# OUTPUT: Hi


# Another one
res = bot.get_response('Good Night!')
print res
# OUTPUT: I am doing well, how about you?
```

The last response doesn't make sense. The training dataset if very short so we need to a more data so the chatbot will fit our purposes. We can use our own data for training. We can use a list where each item in the list is a possible response to its predecessor:

```python
from chatterbot import ListTrainer
bot.set_trainer(ListTrainer)

bot.train(["Good night", "Sweet dreams"])
res = bot.get_response("good night")
print res
# OUTPUT: Sweet dreams
```

You can also export your bot data to a file by running
```
bot.trainer.export_for_training('myData.json')
```








<!-- TODO: sudo apt-get install libmysqlclient-dev-->