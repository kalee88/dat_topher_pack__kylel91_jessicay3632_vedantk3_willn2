# Topher's Tea By datTopherPack
## Roster and Roles:  
|                                        | Kyle L.    | Jessica Y. |  Vedant K. | Will N.  |
| -------------------------------------- | ---------- | ---------- | ---------- | -------- |
| Set up Flask and SQLite3 environment   |    **X**   |            |            |   **X**  |
| Build User Authentication Functionality|            |            |            |   **X**  |
| API Configuration and Connections      |            |    **X**   |            |          |
| Middleware file organization           |            |            |            |   **X**  |
| Middleware creation (actual coding)    |    **X**   |    **X**   |            |          |
| Build Database                         |            |            |            |   **X**  |
| Frontend (HTML Templates)              |    **X**   |            |   **X**    |          |
| Frontend (CSS + FEF)                   |            |            |   **X**    |          |
| Final Testing and Bug Fixing           |    **X**   |    **X**   |   **X**    |   **X**  |
## Description:
Our project is essentially a news site, such as the New York Times, which displays data from a variety of topics including weather, current events, sports, and arts. Each of these pages contain information from reliable APIs, which can all be found in our API knowledge base. In the arts page specifically, we utilize SearchApi so that you can search up any artwork you find interesting and read a description on the web about it. SearchApi will also be used on the sports page to search for specific sports and game sessions for those sports. By logging in to the page, each user can ‘favorite’ their posts to view later, but this feature is not possible if you are not logged in. 
## Install Guide
### Recommended Method: 
We recommend to do this procedure using the Git Clone method. Click the green button in the top right that says "Code". Then, choose "SSH" in the dropdown that appears and copy the URL that is given. Finally, open up your terminal, cd into wherever you desire to hold the folder. Then, type 
```
$ git clone git@github.com:kalee88/dat_topher_pack__kylel91_jessicay3632_vedantk3_willn2.git
```

### Alternate Method: 
This is an alternate method, if you don't prefer the Git Clone method. Go to the green button in the top right again that says "Code". Then, click "Download Zip". Finally, extract the ZIP file from your downloads and place it in your desired directory. 

Reagardless of which method you choose, navigate to the repo folder and type ```$ pip install -r requirements.txt``` to install required dependencies
## Launch codes
Open a terminal window and navigate to this project.
  * Verify that your path looks something like ```~/.../dat_topher_pack_kylel91_jessicay3632_vedantk3_willn2$```
  
Activate a python virtual enviornment (optional but recommended)
1. Launch the terminal.
2. If you do not already have one, run ```$ python3 -m venv {path name}``` to create a virtual environemnt
3. Activate a venv
    * macOS/Linux: `$ source {path_name}/bin/activate`
    * Windows: `$ {path_name}\Scripts\activate`

Activate dotenv 
1. Launch the terminal.
2. Cd into ```~/.../dat_topher_pack_kylel91_jessicay3632_vedantk3_willn2/app/utils$```
3. Run ```$ pip install python-dotenv``` in the terminal.
4. Create an env file and add API keys.

If you want to deactivate the environment, run ```$ deactivate``` 

When you have the virtual enviornment activated:
1. Run ```$ python3 -m app.__init__``` in the terminal
2. Click the link that appears in the terminal to [127.0.0.1:5000](http://127.0.0.1:5000).

