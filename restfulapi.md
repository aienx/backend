# API Endpoints
The web application provides the following API endpoints:

## Shorten URL

 - URL: /api/shorten

 - Method: POST

 - Request Payload:
 ```
  {
    "url": "https://www.example.com/very-long-url-with-lots-of-characters"
  } 
  ```
## Response
 ```
 {
    "original_url": "https://www.example.com/very-long-url-with-lots-of-characters",
    "shortened_url": "https://bit.ly/abcd123",
    "clicks": 0
  }
  ```
  
## Click Statistics
  URL: /api/stats/<shortened_url_id>

  Method: GET

  Response:
  ```
  {
    "original_url": "https://www.example.com/very-long-url-with-lots-of-characters",
    "shortened_url": "https://bit.ly/abcd123",
    "clicks": 10
}
```

# License
 This project is licensed under the MIT License. See the LICENSE file for more details.
