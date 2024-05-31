# Charge Together
## Introduction

When you, as new parents, have just found out that your child has Charge Syndrome, your life is turned upside down and the first information you find online is scary and you feel very alone. 

Therefore, this blog was created and designed for the families and relatives of, children, young people and adults, with Charge Syndrome. 

Here users can write and share their stories and experiences. And as new parents to be able to come to this blog and hopefully get some kind of peace. Because even if the road didn't turn out as they thought, it will still be good in the end and they are not alone!

## Table of Content

- [Introduction](#introduction)
- [Project Goals](#project-goals)
    - [Strategy](#project-goals)
    - [Target Audience](#target-audience)
    - [Site Goals](#site-goals)
    - [User Goals](#user-goals)
- [Agile Planning](#agile-planning)
     - [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
    - [Features](#features)
    - [Future Features](#future-features)
- [Skeleton](#skeleton)
    - [Flowchart](#flowchart)
    - [Wireframes](#wireframes)
    - [Entity Relational Diagram](#entity-relational-diagram)
- [Security](#security)
    - [Cross-Site Request Forgery (CSRF) Protection](#cross-site-request-forgery-csrf-protection)
    - [Django Allauth for Authentication and Authorization](#django-allauth-for-authentication-and-authorization)
    - [Restricted Features for Authenticated Users](#restricted-features-for-authenticated-users)
- [Surface](#surface)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Testing](#testing)
    -[Validation](#validation)
    -[Lighthouse Report](#lighthouse-report)
    - [Responsiveness](responsiveness)
    - [User Stories Testing](#user-stories-testing)
    - [Automated Testing](#automated-testing)
- [Bugs](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Unresolved Bugs](#unresolved-bugs)
- [Credits](#credits)
    - [Websites](#websites)
    - [Resources](#resources)
    - [Images](#images)
    - [People](#people)

## Project Goals

The project aims to create a user-friendly platform for sharing personal stories and experiences about Charge Syndrome, which allows users to read, share, and take part in all the different experiences and stories that exist around this unusual Syndrome.

### Target Audience

The target audience includes parents, siblings, grandparents, aunts, uncles, cousins. Everyone who in some way has a relationship with someone with Charge Syndrome, and who wants to share their own stories and experiences.

### Strategy

- **Project Goals:** Define goals for sharing, reading and managing blog posts.

- **User-Centric Approach:** Understanding the needs of users who have someone in their life with the   Syndrome.

- **Engagement Strategy:** Encourage actions such as liking and commenting on blog posts, to foster a sense of community.

### Site Owner Goals

- Create a vibrant community around Charge Syndrome

- Flag the syndrome to the rest of the world

- Engage users by providing valuable content and features.

- Increase user retention through interactive features and personalized experiences.

### User Goals

- Easily find and read about other people's stories and experiences 

- Share their own stories and experiences with others in the same situation

- Interact with other users by liking and commenting on blog posts.

- Easily navigate between the different pages of the blog and get access to relevant information.

- Have a visually appealing and responsive user interface.

## Agile Planning
### User Stories
## Scope
## Structure
### Features
### Future Features
## Skeleton
### Flowchart
### Wireframes
### Entity Relational Diagram

## Security
### Cross-Site Request Forgery (CSRF) Protection

- Implementing CSRF protection helps prevent malicious websites from executing unauthorized actions on behalf of authenticated users.
- Django provides built-in CSRF protection by including a CSRF token with each form submission and verifying it on the server side.

### Django Allauth for Authentication and Authorization

- Django Allauth is an authentication and authorization framework that provides features like registration, login, password management, and social authentication.
- It ensures secure user authentication and authorization processes.

### Restricted Features for Authenticated Users

- Certain features, such as creating, editing, or deleting blog posts and profiles, are reserved for authenticated users only.
- By requiring users to be logged in to access these features, the application enhances security and ensures that sensitive operations are performed by authorized individuals only.


## Surface
### Design
#### Colour Scheme
#### Typography

## Languages/Technolgies
This Project is built using various technologies.

- **Django 5.0.6:** A Python web framework for building web applications.
- **Bootstrap 5.2.3:** A front-end framework for responsive and visually appealing design.
- **ElephantSQL:** An open-source relational database for data storage.
- **Cloudinary:** Cloud-based storage for the users uploaded images.
- **Heroku:** The platform where the project is deployed.
- **Git and GitHub:** Version control and code repository management.
- **IDE:** Vs Code (Visual Studio Code).

Added libraries can be seen in the requirements.txt file. 
Additionally, custom- python, html, django templating language, and css were all used. 
The README was written using markdown.

## Deployment

- I set up a postgreSQL server at [ElephantSQL.](https://www.elephantsql.com) 
- I made sure to adjust the settings file accordingly, to utilize that database.
- I also made sure to have my SECRET_KEY and DATABASE_URL in the env.py file.
- And made sute to add the env.py file to .gitignore.
- I installed gunicorn version 20.1.0, and added it to the requirements.txt.
- I installed whitenoise version 5.3.0 and added it to the requirements.txt. I also added it to middleware settings file.
- I also created  a path for whitenoise to collect static files in the settings file.
- I Created a Procfile, and declared it as a web process followed by the command to execute the project.
- Added a runtime.txt file to root directory, and added a supported python version as close as possible to my own.
- I run the command collectstatic, to collect static files.
- In the settings file I set **DEBUG = os.environ.get("DEVELOPMENT")** and in env.py I added; **os.environ.setdefault('DEVELOPMENT', 'True')**, so i don´t have to remember to change debug to *False* everytime I deploy to Heroku.
- I added Heroku to allowed hosts in the settings file (.herokuapp). Then I Pushed the code to GitHub.
- I went to [Heroku](https://.heroku.com) and created a new app.
- On the settings tab of my app I clicked "Reveal Config Vars" and added DATABASE_URL and SECRET_KEY.
- The DATABASE_URL got the value of my postgresql database url, and the SECRET_KEY got a complicated value that i made up of my own.
- Then I went back to the deploy tab of my app, and clicked connect to GitHub.
- I then searched for my repository and connected it to the app, and clicked Deploy branch

Here is a link to my Deployed project: 

Cloning or forking this project can be done from my GitHub repository, and 
you need to install the dependencies using the *pip install -r requirements.txt* command.


## Testing
### Validation
### Lighthouse Report
### Automated Testing
### Responsiveness
### User Stories Testing
## Bugs

On the post_detail page I got a bug on the comment function, I couldn't leave a comment from the frontend

![bug1](documentation/images/bug_1.png)

### Solved Bugs
In my view, I had only linked comments to the blog post itself. I fixed the bug by also linking the comment to the user.

![bug1](documentation/images/fixed_bug_1.png)

### Unresolved Bugs
I currently have no bugs I am aware of.
## Credits
### Websites
### Resources
### Images
### People