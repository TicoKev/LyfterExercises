# Internet Fundamentals

## 1. From Client to Server
1. What does the client (browser) do?
  The browser sends a request to the server.
2. What role does the DNS play?
  The DNS servers are responsible for translating the domain names into IP addresses.
3. What happens with the IP address?
  The browser send a request using the IP obtained from the DNS.
4. What does the server do?
  The server sends the response back to the client with the content of the page, allowing the access to YouTube.

## 2. Frontend and Backend in Action
  The fronted would be the section where a customer can create the appointment, check availability, choose the requiered service. 
  Also, if an appointment is already created the customer should be able to edit or delete it all of this happens be in the frontend. 
  POssible technologies for the frontend: JS/TS, React, TailwindCSS.
  The backend is where all the information is stored, such as appointment details, availability, personal information of customers and doctors. 
  And we can use python, postgresql and django.
  The way the frontend interacts with the backend is through APIs. For example when a customer wants to create an appointment the application
  sends a POST HTTP request to the server`s API. The backend receives the request and checks fot the availability and then stores the 
  appoitnment information in the DB. The server responds with a confirmation.

## 3. REST vs SOAP vs GraphQL

| API Type   | Data Format Used | Level of Flexibility | Implementation Difficulty | Current Usage (High / Medium / Low) |
|------------|------------------|----------------------|---------------------------|--------------------------------------|
| REST       |     JSON         |        High          |          Low              |                  High                |
| SOAP       |     XML          |        Low           |          High             |                  Low                 |
| GraphQL    |     JSON         |        High          |          Medium           |                  Medium              |

**Which is more appropriate for a modern startup? Why?**
  REST is the better option for a modern startup because it is simple to implement, and easy to use.  
  It uses lightweight data formats like JSON, which makes communication fast and efficient. 

## 4. Exploring APIs with Postman

### 4.1 API Selection
- **API Name:** JSONPlaceholder
- **Description:** Is a free online REST API used for practice with fake data.

### 4.2 Postman Setup
- **Collection Name:** JSONPlaceHolder
- **Requests Added:**
  - GET - 
  - POST -
  - DELETE -

### 4.3 Execution and Analysis

| Request | Method | Endpoint                                        |    Status Code |   Notes                                                     |
|---------|--------|-------------------------------------------------|----------------|-------------------------------------------------------------|
|  GET    |  GET   |  https://jsonplaceholder.typicode.com/posts     |     200        |   Returns all posts in JSON format                          |
|  POST   |  POST  |  https://jsonplaceholder.typicode.com/posts     |     201        |   Creates a new post and the API returns the object created |
|  DELETE | DELETE |  https://jsonplaceholder.typicode.com/posts/101 |     200        |   Deletes the post                                          |
### 4.4 Technical Explanation
  The API used was JSONPlaceHolder, is an API which has fake data where it can be used to practice HTTP methods.
  I tested the following methods:
  GET: retrieved all posts using https://jsonplaceholder.typicode.com/posts and confirmed the response body structure (userId, id, title, body).
  POST: created a new post using  https://jsonplaceholder.typicode.com/posts and received a simulated id in the response.
  DELETE: simulated the deletion of a post using  https://jsonplaceholder.typicode.com/posts/101, receiving an empty JSON object as confirmation

#### [Request Name]
- **HTTP Method:** POST
- **Endpoint:** https://jsonplaceholder.typicode.com/posts 
- **Parameters / Body:**   
  {
    "title": "new post",
    "body": "This a new post in the JSONPlaceHolder API",
    "userId": 1798
  }
- **Response Description:**   
  {
    "id": 101,
    "title": "new post",
    "body": "This a new post in the JSONPlaceHolder API",
    "userId": 1798
  }

**What did you learn from the process?**
  This exercise was very helpful to understand how to interact with APIs using Postman and different HTTP methods. By working with the JSONPlaceholder API, 
  which provides fake data, I was able to simulate real-world API behavior.
  
### 4.5 Final Reflection
  1. I learned that APIs are the bridge between clients and servers, allowing structured communication through HTTP methods. By practicing with 
  JSONPlaceholder, I understood how requests and responses are formatted in JSON, and how different methods (GET, POST, PUT, DELETE) simulate real-world 
  operations such as retrieving, creating, updating, and deleting data. This helped me see that not all REST APIs are identical, so it is important to 
  analyze the format and requirements of each one before interacting with it.
  2. Postman made this process much more intuitive by letting me manually send requests and immediately inspect the responses, status codes, and headers. 
  Instead of only reading frontend code that fetches or manipulates data, I could directly experience the underlying communication flow. This hands-on 
  approach clarified how APIs work behind the scenes and gave me confidence to understand client-server interactions in future projects.