# CrowdHarbour Back End: Funding Waves of Social Change

Repository for the backend of the She Codes Crowdfunding project, utilizing the Django Rest Framework.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)&nbsp; ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) &nbsp; ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) &nbsp; ![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE)

### About

CrowdHarbour is a web application that provides a platform for social impact initiatives to raise funds for their projects.

### Intended Audience/User Stories

Those seeking to raise awareness and gather financial support for their projects that have a meaningful impact on social wellbeing.
These initiatives target social issues and aim to create positive and lasting changes in society.
These initiatives might focus on providing greater education access or promoting environmental sustainability for example.

### Front End Pages/Functionality

- {{ A page on the front end }}
  - {{ A list of dot points showing functionality is available on this page }}
- {{ A second page on the front end }}
  - {{ A list of dot points showing functionality is available on this page }}

### API Spec

| **URL**        | **HTTP Method** | **Purpose**                          | **Request Body** | **Success Response Code** | **Authorizon/Authentication** | **Implemented Yet** |
| -------------- | --------------- | ------------------------------------ | ---------------- | ------------------------- | ----------------------------- | ------------------- |
| /projects/     | GET             | Returns all projects.                | N/A              | 200                       | None required                 | Yes                 |
| /projects/     | POST            | Create a new project.                | Project object.  | 201                       | Must be logged in             | Yes                 |
| /projects/1/   | GET             | Returns the project with ID of "1".  | N/A              | 200                       | None required                 | Yes                 |
| /projects/1/   | PUT             | Updates the project with ID of "1".  | Project object.  | 202                       | Must be logged in             | Yes                 |
| /pledges/      | GET             | Returns all pledges.                 | N/A              | 200                       | None required                 | Yes                 |
| /pledges/      | POST            | Create a new pledge.                 | Pledge object.   | 201                       | Must be logged in             | Yes                 |
| /pledges/1/    | GET             | Returns the pledge with ID of "1".   | N/A              | 200                       | None required                 | Yes                 |
| /categories/   | GET             | Returns all categories.              | N/A              | 200                       | None required                 | Yes                 |
| /categories/1/ | GET             | Returns the category with ID of "1". | N/A              | 200                       | None Required                 | Yes                 |

---

## Contact Me

If you have any questions regarding the project or would like to get in touch, please refer to my contact information below.

<a href="mailto:blakerach1@gmail.com"><img alt="email link" src="https://img.shields.io/badge/EMAIL-%23ba03fc?style=for-the-badge" target="_blank" /></a>
<a href="https://github.com/blakerach1"><img alt="GitHub badge" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" target="_blank" /></a>
