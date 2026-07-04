## **MPEI Info Bot Docs** ##

### Getting Started ###
Firstly clone this repository<br>

Copy cloning link ```https://github.com/Oceangrad/MPEI-Telegram-Bot.git``` then open a directory where you want to put this project.<br>

Open a command line inside your directory and write a command ```git clone https://github.com/Oceangrad/MPEI-Telegram-Bot.git```<br>
**(NOTE that you have to install python and Git to your PC first)**<br>

### Modules installation ###
#### Now that you've cloned the repository lets import modules needed to start the bot ####
To install modules required for bot to work you need to install the reqirements.<br>

Simply go back to your directory where you cloned repository and open a command line.<br>
Then write a command ```pip install -r requirements.txt```<br>

It will install all the modules that project requires to work.

### Configuring a Database ###
#### Project requires a database to work ####
Project needs PostgreSQL database to work.<br>
Obviously you need to install PostgreSQL to your PC first<br>
**(NOTE THAT YOU SHOULD SAVE POSTGRES' LOGIN AND PASSWORD. OTHERWISE YOU WON'T BE ABLE TO ACCESS A DATABASE)**<br>

**You can install Postgres [here](https://www.postgresql.org/download/ "PostgreSQL download link")!**<br>
(Recomended version is Postgres16)

After you installed Postgres launch pgadmin4 and go to Servers > Postgres16 > Databases<br>
You need ```postgres``` database. Right-click it and click on Query Tool.<br>

Now query window should open. Paste there this database-creation-query:<br>
```sql
CREATE DATABASE tg_project
    WITH
    OWNER = [put your postgres username here]
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United Kingdom.1251'
    LC_CTYPE = 'English_United Kingdom.1251'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```
and execute the script (You can press F5 to execute the open script)
##### **(DONT FORGET TO CHANGE OWNER PROPERTY TO YOUR DATABASE USERNAME)**<br>
```tg_project``` database should be created.<br>

Now go to tg_project's Query Tool and paste there this table-creation-query:<br>
```sql
CREATE TABLE public.users
(
    id serial NOT NULL,
    user_id numeric(25),
    student_group character varying(35),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.users
    OWNER to [put your postgres username here];
```
and execute the script.
##### **(DONT FORGET TO CHANGE OWNER PROPERTY HERE EITHER)**<br>

Table "```users```" should be created.<br>
**Now database should be ready to work.**

### Configuring the project ###
**(Thats an important part too)**
#### Lets create a config file ####
Now that you've created a database for this project you can proceed to create a config file.<br>

Create a file inside your directory called "```config.ini```"<br>
Then copy everything from file ```config_template.ini``` into ```config.ini```<br>
When you copied everything you dont need ```config_template.ini``` anymore. You can delete it whenever you like.<br>

Now open ```config.ini``` file and find ```[SECRET.DATABASE]``` section.<br>
For bot to actually work you need to fill this whole section with your database credentials.<br>

You can find ```host``` and ```port``` at properties of Postgres16 server<br>
(Servers > Postgres16 > Right-click > Properties > Connection tab)<br>

```dbname``` is simply a database name. If you didn't change the database name it should still be "```tg_project```".<br>

```user``` and ```password``` properties are login props for Postgres16 (which you put while installing postgres)<br>
**Database properties should be ready for now**<br>

Last thing to configure is ```token``` at [SECRET] section. It's a Bot Token for telegram.<br>
To get a bot token go to your Telegram App and send a message to a @botfather and send the ```/new_bot``` command. Then follow it's instruction.<br>
In the end you should get your Bot Token from @botfather which you should put into ```token``` property of ```config.ini``` file.

### Launching this Bot ###

#### Now that you followed all of these instruction we can start this bot ####
**(Note that if you skipped some of the instruction this bot is NOT going to work correctly)**

To start the bot simply open a command line inside bot directory and put ```python main.py``` command.<br>

The bot should launch correctly.
Now go to Telegram App and send a ```/start``` message to your bot.
