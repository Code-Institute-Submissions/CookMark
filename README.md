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
* Materialize Teal, used for form:active and buttons.
* Materialize Red, used for delete button and incorrect form input if required input.
* Materialize Green, used for valid form input.
* Materialize Blue, Used for edit, changed it into blue, as blue represents security and therefore suggests "it¨'s safe to change the document".

#### Fonts

Raleway and Roboto are the project fonts. They were put together by using [FontPair](https://fontpair.co/), a free font pair tool.
Raleway is used for headers and Roboto for main text for a good readability. However, the Raleway font in h5 needed an increased
letter-spacing due to the letters molding into each other a bit.

## Technologies Used

The project was made in Visual Studio Code, where a virtual environment was set up.

### Languages

HTML5, CSS3, Python 3.8.5 and JavaScript.

### Frameworks

[Materialize](https://materializecss.com/) was used as the main frontend framework. In later iterations of the wireframes I planned them out with the materialize design as a basis. Both the CSS and JS was used.

[Flask](https://flask.palletsprojects.com/en/1.1.x/) was the micro framework used with Python.
Jinja was used as a template language, which reduced a lot of code as a base template was designed and the other templates were extended from the base.

