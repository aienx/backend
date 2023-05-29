### Web Frameworks Project: URL Shortening / Flask python

![Project Name](https://github.com/aienx/backend/blob/main/url.png =300x200)

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
