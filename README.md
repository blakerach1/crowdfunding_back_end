# CrowdHarbour Back End: Funding Waves of Social Change

Repository for the backend of the She Codes Crowdfunding project, utilizing the Django Rest Framework.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)&nbsp; ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) &nbsp; ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) &nbsp; ![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE)

### About

CrowdHarbour is a web application that provides a platform for social impact initiatives to raise funds for their projects.

### Intended Audience/User Stories

Those seeking to raise awareness and gather financial support for their projects that have a meaningful impact on social wellbeing.
These initiatives target social issues and aim to create positive and lasting changes in society.
These initiatives might focus on providing greater education access or promoting environmental sustainability for example.

## Deployed Project Link

https://crowdfunding-back-end-424.fly.dev/projects/

## Interacting with API via Insomina

URL: https://crowdfunding-back-end-424.fly.dev/projects/

## Interacting with API via Django REST Framework Interface

### Successful GET request of USER endpoint

![Image of successful GET request for users endpoint](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_get_users.png?raw=true)

### Successful POST request of USERS endpoint

![Image of successful POST request for users endpoint](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_post_users.png?raw=true)

### Successful POST request to obtain token

![Image of successful POST request for token endpoint](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_post_token.png?raw=true)

## Creating a New USER

### Using Insomnia

![annotated image of creating a new user via Insomnia](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_Create_User_Insomnia.png?raw=true)

#### 1. Set up a new POST HTTP request and enter: https://crowdfunding-back-end-424.fly.dav/users/ into the URL bar.

#### 2. Populate the "JSON" body field with user data in JSON format.

#### 3. Once you have entered at least the username, first_name, last_name, email and password for your user, Click send.

### Using Django REST Interface

![annotated image of creating a new user via Django REST interface](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_Create_User_API.png?raw=true)

#### 1. Enter the following in your web browser: https://crowdfunding-back-end-424.fly.dav/users/.

#### 2. Populate the "JSON" body field with user data in JSON format.

#### 3. Once you have entered at least the username, first_name, last_name, email and password for your user, Click post.

![image with successful response for user creation](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_Create_User_API_1.png?raw=true)

## Creating a New PROJECT

### Using Insomnia

![first annotated image of creating a new project via Insomnia](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_Create_Project1_Insomnia.png?raw=true)

#### 1. Set up a new POST HTTP request and enter: https://crowdfunding-back-end-424.fly.dav/projects/ into the URL bar.

#### 2. Populate the "JSON" body field with project data in JSON format.

#### 3. Enter your user token under the "bearer" tab.

#### 4. Once you have entered at least the title, description and goal for your project Click send.

![second annotated image of creating a new project via Insomnia](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour_Create_Project2_Insomnia.png?raw=true)

### Using Django REST Interface

#### 1. Enter the following in your web browser: https://crowdfunding-back-end-424.fly.dav/projects/.

#### 2. Populate the "JSON" body field with project data in JSON format.

#### 3. Once you have entered at least the title, description and goal for your project Click post.

### API Spec

| **URL**        | **HTTP Method** | **Purpose**                          | **Request Body** | **Success Response Code** | **Authorizon/Authentication** | **Implemented Yet** |
| -------------- | --------------- | ------------------------------------ | ---------------- | ------------------------- | ----------------------------- | ------------------- |
| /users/        | GET             | Returns restricted info on users.    | N/A              | 200                       | None required                 | Yes                 |
| /users/        | GET             | Returns all info on all users.       | N/A              | 200                       | Must be an admin user         | Yes                 |
| /users/        | POST            | Creates a new user.                  | N/A              | 200                       | None required                 | Yes                 |
| /users/1/      | GET             | Returns restricted info on user "1". | N/A              | 200                       | None required                 | Yes                 |
| /users/1/      | GET             | Returns all info on user "1".        | N/A              | 200                       | Must be an admin user         | Yes                 |
| /users/1/      | DELETE          | Deletes a User.                      | N/A              | 202                       | Must be user or admin user    | Yes                 |
| /projects/     | GET             | Returns all projects.                | N/A              | 200                       | None required                 | Yes                 |
| /projects/     | POST            | Create a new project.                | Project object.  | 201                       | Must be logged in             | Yes                 |
| /projects/1/   | GET             | Returns the project with ID of "1".  | N/A              | 200                       | None required                 | Yes                 |
| /projects/1/   | PUT             | Updates the project with ID of "1".  | Project object.  | 202                       | Must be logged in             | Yes                 |
| /pledges/      | GET             | Returns all pledges.                 | N/A              | 200                       | None required                 | Yes                 |
| /pledges/      | POST            | Create a new pledge.                 | Pledge object.   | 201                       | Must be logged in             | Yes                 |
| /pledges/1/    | GET             | Returns the pledge with ID of "1".   | N/A              | 200                       | None required                 | Yes                 |
| /categories/   | GET             | Returns all categories.              | N/A              | 200                       | None required                 | Yes                 |
| /categories/   | POST            | Create a new category.               | Category object. | 200                       | Must be an admin user         | Yes                 |
| /categories/1/ | GET             | Returns the category with ID of "1". | N/A              | 200                       | Must be an admin user         | Yes                 |
| /categories/1/ | PUT             | Updates the category with ID of "1". | Category object. | 202                       | Must be an admin user         | Yes                 |

---

### Database Schema

![image of database schema for the project](https://github.com/blakerach1/crowdfunding_back_end/blob/main/imgs/CrowdHarbour.drawio.png?raw=true)

### Front End

Stage 2 of this project was to create a React JS frontend that interacts with this backend application. See the frontend repository here: https://github.com/blakerach1/crowdfunding-frontend


## Contact Me

If you have any questions regarding the project or would like to get in touch, please refer to my contact information below.

<a href="mailto:blakerach1@gmail.com"><img alt="email link" src="https://img.shields.io/badge/EMAIL-%23ba03fc?style=for-the-badge" target="_blank" /></a>
<a href="https://github.com/blakerach1"><img alt="GitHub badge" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" target="_blank" /></a>
