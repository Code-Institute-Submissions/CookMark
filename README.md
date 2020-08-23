# CookMark, your interactive recipe website

The purpose of the project stems from an issue of mine. One of most loved hobbies is cooking, however I've
noticed my bookmarks of several recipe pages are starting to rile up and I end up scrolling, trying to find the recipes in the 
small bookmark text. Therefore, the purpose of this project is storing your own favorite recipes of what you've found on the
internet.

## UX

### User Stories

As a user...
Navigation and viewing:
1. I want to easily find essential functions.
2. Be able to go back to the home page.
3. View the most important parts of the recipe, so I can read more if I want to.
4. An uncluttered page, to minimize potential frustration.
5. Find contact information easily.
CRUD:
6. I want to be able to add my own recipes with almost no restrictions.
7. It would be great to sort my information according to preferences.
8. If I'm completely unhappy, I need to remove the information I've added previously.
9. I need to be able to update my recipe with notes for instance.
Interaction:
10. Visual cues are a good way to see things are working as they should.
11. Responsive design is appriciated, as I can then use my phone, tablet or desktop for the app without any "friction".

### Not implemented
* Collections, for a user to create their own collection and thereby be able to sort the recipes better.
* Sorting system, using data such as difficulty to sort the recipes from each other.
* Contact Modal

### Design

The design process was to first begin with pencil sketches, where I made the initial wireframes and
ideas for the CookMark logo. After having a rough idea of what I wanted, I made the wireframes digital in [Figma](https://www.figma.com).
Figma is really a great tool when working a lot with frontend. Helps to plan out the app's responsiveness.

My main goal with the website design was to make it easily manageable and practical for the user. As I want to have one, go-to place
where I can store all of my recipes there's no need for anything "too" fancy.

Initial sketches: [First](https://drive.google.com/file/d/18DDM5ZiD4tCTSZCwCe1MpnvewNAoSf4m/view?usp=sharing) [Second](https://drive.google.com/file/d/18A7ioOm_vt7fxoxnPNi4l5MzQnsWRd9k/view?usp=sharing)

#### Wireframes

I had several irriterations of the wireframes, here's a little snippet of what my first iterations looked like.
Earlier versions:
[1](https://drive.google.com/file/d/1b_2uMTVPzaG_nsk-03E6PryT2CAq8TIF/view?usp=sharing), [2](https://drive.google.com/file/d/1soYYrKWzvnWrLN7zkXuqYbrZ3l9P44aA/view?usp=sharing), [3](https://drive.google.com/file/d/1Qh01iyiNuAHiitf2KEjXeEa5_q9QKSKf/view?usp=sharing), [4](https://drive.google.com/file/d/1VQR8mOIY1e8XOHl98nhXJPgZ39liEtbl/view?usp=sharing).

The wireframes are meant to give a sense of how the structure of the page was going to be.
In earlier versions I explored colours more.

[Final wireframes for desktop, tablet and phone](https://drive.google.com/file/d/1oZ5TibaK7Et70dM39TGwY92WgD-3rbA6/view?usp=sharing) with resolutions:
- Desktop, 1440 x 1024
- Tablet, 768 x 1024
- Phone (Android) 360 x 640

Changes from the wireframes include:
* Moved the logo to the middle of the navbar and hamburger nav to the left instead of right.
* Removed the contact modal due to time restraints.
* Removed sorting bar in home page due to insufficient time.
* Included the card view in the viewing recipe page, which is also used in the home page for repeating practices.
* Photo url replaced file upload selection and recipe url was added.
* The delete button was removed from the home page and moved to the get recipe page. It's due to less clutter on the home page and also as it's less of a chance that a user would delete their own recipe.


#### Illustrations

Logo: The CookMark logo is meant to represent the main idea of the project, bookmark + food.
The bookmark is represented in the shape of the logo, so when it sits on the top of the page, it resembles a bookmark
hanging down from the navbar. Food comes from the inner, cut-out shape of a fork, which is also the shape of an M.
What I'm content with are the cut-out C and fork(M) in the logo, as they are the initials for CookMark.

Other illustrations: The girl on the home page is from [undraw](https://www.undraw.com), which is free for non-commercial use.

#### Colours

Less colours than usual was used for the project, there was a less need for complementary colours that "pop", as the website isn't trying to sell anything or make you sign up for something. To make the code more readable, I used sass-variables for my colour scheme.
Instead of using a lot of dark text, I went with white text instead to make the website have a lighter feel to it.

Specialized colours: 
* #85be8b or $lightgreen: One of the main colours of the project, together with white.
Green shades were implemented in the project as it's relaxing and calming for the eye.
Was used 
* #70ac76 or $darkgreen: Used for the navbar.
* #ffffff or $white: A lot of white was used for instance, to highlight the meaning of the page, such as "Edit recipe".
* #888888 or $gray: For the cards, a soft gray was used for the text, as it 

Materialize colours:
* Materialize Teal, used for form:active.
* Materialize Red, used for delete button and incorrect form input if required input.
* Materialize Green, used for valid form input.
* Materialize Blue, Used for edit and add buttons, as blue represents security and therefore suggests "it's safe to change the document".

#### Fonts

Raleway and Roboto are the project fonts. They were put together by using [FontPair](https://fontpair.co/), a free font pair tool.
Raleway is used for headers and Roboto for main text for a good readability. However, the Raleway font in h5 needed an increased
letter-spacing due to the letters molding into each other a bit.

## Technologies Used

The project was made in Visual Studio Code, where a virtual environment was set up.
The database used was MongoDB, which is a document oriented database. The structure of data was put into:
- main 
-- recipe collection (main collection)
-- other collections (which were all called and used for inserting data into recipe collection)

### Languages

HTML5, CSS3, Python 3.8.5 and JavaScript.

### Frameworks

[Materialize](https://materializecss.com/) was used as the main frontend framework. In later iterations of the wireframes I planned them out with the materialize design as a basis. Both the CSS and JS was used.

[Flask](https://flask.palletsprojects.com/en/1.1.x/) was the micro framework used with Python.
Jinja was used as a template language, which reduced a lot of code as a base template was designed and the other templates were extended from the base.

### Libraries

JQuery was used for JavaScript.

### Style Sheet

Sass was used to reduce the code and workload with the help of variables and built-in optimization for other browsers. An extention in Visual Studio Code was needed.

## Testing

The initial thought was to implement some Jasmine testing, however time constraints made me not continue with Jasmine and I therefore used other testing resources. 

### General testing
For general code testing, I've used several testing apps.

- Html testing: [Html validator](https://www.freeformatter.com/html-validator.html), no bugs were found. However, responded with a lot of errors as Jinja was used.
- Css testing: [Jigsaw](https://jigsaw.w3.org/css-validator/validator), no bugs were found. [CssLint](http://csslint.net/), got errors "heading should only be defined once" and "Disallow IDs in selectors". I found these notifications to be alright and does not majorly disrupt the code.
- [Responsiveness testing](https://www.responsinator.com/?url=https%3A%2F%2Fcook-mark.herokuapp.com%2F), works on desktop, tablet and mobile.
- Using Debug in python code.

### Testing combined with user stories

As a user...
1. "Be able to go back to the home page." - Works by clicking the navbar, both in mobile and desktop view. The logo can also take you back to the home page.
2. "I want to be able to add my own recipes with almost no restrictions." - The Create (Add) function works and inserts the new info into MongoDB without any issues. Almost no restrictions means that not all form inputs are required, which they aren't.
3. "If I'm completely unhappy, I need to remove the information I've added previously." - The Delete function works and is placed in the get recipe page. Deletes the recipe record from MongoDB.
4. "I need to be able to update my recipe with notes for instance." - The Edit function works and updates the data in MongoDB.
5. "Responsive design is appriciated, as I can then use my phone, tablet or desktop for the app without any "friction"." - The responsive design was tested with [responsinator](https://www.responsinator.com/?url=https%3A%2F%2Fcook-mark.herokuapp.com%2F).

## Deployment

The project was deployed on Heroku. Version control was done with Git and GitHub pages.

### Deployment Steps

The project was deployed on Heroku and the CookMark Heroku app is connected to GitHub as deployment method. It was initially supposed to be deployed using the Heroku CLI push, however it didn't work for me atleast after hours of trying.

**Creating virtual environment:**
- Created a directory where the flask app was supposed to be
- Changed directory to the flask app, C:\Users\Karolina\Documents\Programming projects\cookmark
- In the Command Prompt: `>py -m venv env, hit enter`
- Then: >env\Scripts\activate, hit enter
- Installed flask by: `>pip install flask`
- Created app.py in the directory
- In the Command Prompt: `>set FLASK_APP=app.py`

**In Vs Code:**
- Opened up app.py in VS Code and inserted "from flask import Flask" at the top of the page
- In terminal: `$ pip freeze --local > requirements.txt`, for Heroku to be able to install the needded packages to run the app.
- In the line below, wrote `app = Flask(__name__)`
- Created an app route
- Created env.py and wrote **import os** at top
- Then `os.environ["MONGO_DBNAME"] = 'YOUR_MONGO_DB_PROJECT_NAME'`
and after, `os.environ["MONGO_URI"] = 'YOUR_SRV_CODE_IN_MONGO_DB'`
- In app.py put:
```
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')

app.config["MONGO_DBNAME"] = MONGO_DBNAME
app.config["MONGO_URI"] = MONGO_URI
```
- Created a .gitignore file and put files which shouldn't be seen by the public, such as "env.py" in there before I pushed.

**GitHub:** 
In terminal:
-  `$ git init`, to initialize git
```
$ git remote add origin <URL_OF_GITHUB_REPO>.git
$ git push -u origin master
```
For commits and pushes, I used GitHub desktop (great program which makes git easy to handle).

**Mongo DB:**
- Created a new collection in Cluster which was connected with the secret keys created.

**Heroku:**
- Created a new app in Heroku
- Set env variables by going to Settings -> Config Vars -> Reveal Config Vars
- Created vars for: IP, PORT, MONGO_DBNAME, MONGO_URI
In terminal: 
- `$ heroku login` where I put in my heroku info
- `$ git init` to initialize git repo
- `$ heroku git:remote -a <NAME_OF_APP>` to connect app with heroku, gives link
(The next steps would be commit and push messages, however they didn't work for me so I had to deploy and commit from my GitHub repo)
- `$ touch Procfile`, creates Procfile (IMPORTANT NOTE: many are experiencing issues with Windows 10 and the Procfile. Therefore, create a new Procfile.txt and save, delete the one just created and rename the Procfile.txt -> Procfile. Seems redundant, but solved my "Can't find Procfile" issue. [More info](https://stackoverflow.com/questions/15790691/procfile-not-found-heroku-python-app))
- Wrote `web python app.py` at the top of the Procfile
- In app.py, wrote at the bottom of the python file:
```
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port = int(os.environ.get('PORT', 5000)),
    debug=True)
```
This is to connect with the IP and PORT vars.
- Then in Heroku Dashboard -> Deploy -> Deployment method: Github and followed the instructions. This made all of my pushes to the GitHub repo connect and build on the Heroku app.
- Checked the Automatic deploys and after a successful build -> Open App.
- It was then successfully deployed to Heroku. 

#### How to run it locally
For running the project locally, you'll needed to have Git, the Heroku CLI pre-installed and a text handling program, such as VS Code.

For windows:
[Cloning a repository using the command line](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
You'll also need to create a virtual environment, as written out in the section above.

- On GitHub, navigate to the main page of the repository.
- Above the list of files, click (download symbol) Code.
- To clone the repository using HTTPS, under "Clone with HTTPS", click (copy symbol). To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click (copy symbol).
- Open Git Bash.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier.
`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
- Press Enter to create your local clone.
- Follow the virtual env setup in "deployment section".
- Create env.py
- In env.py, write **import os** at the top.
Then `os.environ["MONGO_DBNAME"] = 'YOUR_MONGO_DB_PROJECT_NAME'`
and after, `os.environ["MONGO_URI"] = 'YOUR_SRV_CODE_IN_MONGO_DB'`
- Then create a .gitignore file, where you want to put all of the secret files.

In terminal: 
- `$ pip install flask` to install the flask library
- `$ pip freeze --local > requirements.txt` to create a requirements.txt file for app dependencies
- `$ flask run`

For Heroku Deployment and MongoDB setup, read the deployment section.
Remember, after each newly installed package, the requirements.txt needs to be updated with:
`$ pip freeze --local > requirements.txt` as otherwise Heroku won't have the required dependencies.

## Credits
- StackOverflow, for answering numerous of questions. 
- W3schools, the same as above. 
- Code institute, for providing the main CRUD idea. 
- Code Institute Slack, great community where a lot of my questions were answered by previously asked questions.
