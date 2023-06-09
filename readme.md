<h1 align="center">Backend / APi Archive </h1>

<h3 align="center">Tools:</h3>
<p align="center"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </p>

Collection of backend and api projects to demonstrate skill sets, knowledge and problem solving scenarios.

## Contents

- Programming language: programming in Python language, python web frameworks (Django and Flask), web scraping, data analysis, machine learning,
  scripting and automation, API development, testing and debugging, database integration, collaboration using version control, and problem-solving.
  <br>
  [Python Archive →](https://github.com/aienx/python-archive)
- Web framworks: working with web frameworks including Flask, Django, and React, with demonstrated experience in building scalable and efficient web 
  applications, utilizing advanced features and integrations, and leveraging powerful tools and libraries within each framework.
  <br>
  [Frameworks Prjs →](./frameworks.md)
- Database: database development, DBMS (MySQL, PostgreSQL, Oracle).
- Restful APi's: Developing intuitive and well-structured APIs, documenting, integrating with third-party APIs, implementing API security measures,
  managing API versioning effectively, optimizing API performance, monitoring and analyzing API usage, and providing real-world examples of API projects.
  <br>
  [Restful Api →](./restfulapi.md)
- Version control: Proficient in Git, experienced with branching strategies and collaboration, knowledgeable in Git workflows, 
  integration with other tools, and documentation practices, personal projects and contributions.
- Testing and degugging: Testing and debugging with expertise in test automation, unit testing, debugging techniques, bug tracking, 
  CI/CD integration, and test case design.
- Backend Security: Implementing secure coding practices, authentication/authorization mechanisms, data encryption, secure APIs, 
  vulnerability assessment, compliance, secure session management, configuration hardening, threat modeling, and incident response.
- Dep and DevOps: Deployment and DevOps, cloud platforms, infrastructure automation, containerization,
  CI/CD pipelines, monitoring, security, and collaboration.
  <br>
  [Cloud DevOps →](https://github.com/aienx/cloud-devops)

### Web Frameworks Project: URL Shortening / Flask python

![Project Name](https://github.com/aienx/backend/blob/main/url.png)

This is a URL shortening web application built with Python Flask. It utilizes the Bitly API for shortening long URLs.

#### Features

- Shorten long URLs to compact, easy-to-share links.
- Track click statistics for each shortened link.
- Easy-to-use web interface.

#### Technologies Used

- Python Flask: A micro web framework for building web applications in Python.
- Bitly API: A URL shortening service that provides an API for programmatic access.

#### Setup Instructions

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/url-shortener.git
   ```
2. Install the required dependencies:
    pip install -r requirements.txt
    
3. Obtain a Bitly API key by signing up for an account at Bitly and create a new application to get the API key.

4. Update the configuration file with your Bitly API key:
    config.py
    BITLY_API_KEY = 'your-api-key'
5. Start the Flask development server:
    flask run
6. Open your web browser and navigate to http://localhost:5000 to access the web application.
7.
[View Project](link-to-project1)

### Web Frameworks Project: Personal Project ( Blog Platform )

![Project Name](https://github.com/aienx/backend/blob/main/blog.png)

## Blog Website

This is a simple blog website built with Python Flask and a personal API created using the npoint platform.

### Installation

1. Clone the repository: `git clone https://github.com/username/blog-website.git`
2. Navigate to the project directory: `cd blog-website`
3. Install the required dependencies: `pip install -r requirements.txt`

### Usage

1. Set up the environment variables required for the Flask application.
2. Run the Flask application: `python app.py`
3. Open your web browser and visit `http://localhost:5000` to access the blog website.

### Features

- User registration and authentication system.
- Create, read, update, and delete blog posts.
- Display a list of blog posts with pagination.
- View individual blog posts and leave comments.
- API endpoints for accessing blog posts and comments.

### Technologies Used

- Python
- Flask
- npoint (for creating the personal API)
- HTML/CSS
- JavaScript

### Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

### License

This project is licensed under the [MIT License](LICENSE).
