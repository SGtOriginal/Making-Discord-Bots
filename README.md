# Making-Discord-Bots

Welcome to documentation #1 of Making Discord Bots, the detailed describtion on how to make Discord Bots easily and deploy them.



I assume that you have Python 3, version 3.8.6.
If you don't have Python 3, then follow these steps:

If you are using Windows, then download it from https://www.python.org/download/releases/3.0/ 
If you are using Linux, then do 'apt-get install python3 python3-pip'
If you are using Mac, then download it https://www.python.org/downloads/mac-osx/ 

Stage 1:

1: Download the files.

2: Put all the files in one single folder.

Stage 2:

1: Go to https://discord.com/developers/

2: Open a new application

3: Put a name for the application

4: Now go to the Bot sub-part

5: Click on Add Bot and confirm

6: Give your bot the permissions it requires

7: Now go to OAuth2 sub-part

8: In the Scopes under OAuth2 URL Generator, click the checkbox beside bot, give it the permissions it requires by scrolling down and copy the url generated.

9: Copy the link generated and paste it in the Redirects section.

10: Click on the Select Redirect URL and click on the first option.

11: Go to the Bot sub-part and copy the bot token.

Stage 3:

1: Open the discord-bot.py file in the folder you put it in.

2: In line 37, remove Paste bot token here and paste your bot token

3: Go to line 5, remove Put your bot prefix here and put a symbol accessable by both mobile and computers, like '!'

4: Save the file

Stage 4:
1: Open a private repository in GitHub and remember the name.

2: Upload all the files you downloaded from my repository, including the python file you updated, on your main branch.

Stage 5:

1: Go to www.heroku.com

2: Get yourself an account.

3: Go to your dashboard and click New and the New App

4: Give it a name, choose a region and click on Create App.

5: Go to Settings, scroll down to Buildpacks, click Add Buildpack, click on Python and then click on Save Changes.

6: Go to Deploy and click on Connect to GitHub.

7: Put in your bot repository and click Search.

8: Select the correct repository from the options and click Connect.

9: Click Enable Automatic Deploys and then click Deploy branch.

10: Wait for it to build itself and it should be successful.

11: Scroll up to the top of the same page and click Resources.

12: Under Free Dynos, click on the Pen button, then on the slider and then click Confirm.

Stage 6:
1: Now go back to https://discord.com/developers/ , then to your bot application, go to OAuth2, copy your Redirect URL from the Redirects already added and paste it in a new tab.

2: Add your bot to your server and Authorize its access.

3: Now open Discord, go to the server you added your bot to and you should see the bot online.



Thank you for following my tutorial. I hope it helped you a lot!

- SGt Original



To contact me:
Discord: SGt Original#2252

Email: sgtoriginal@gmail.com (High possibilty of not answering back :) )
