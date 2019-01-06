### Migration Documentation

1. Data Generation

2. MongoDB 

3. ```d3.js``` and ```chart.js``` implementation

4. ```Node.js``` and ```express.js```

5. Dynamic dashboard


### Application components

Server & Application Starter : 
( Server.js: Node.js, Express.js and MongoDB)


#### Required Modules

Implemented builtin modules :

<b> Express:</b> Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. Read more 

```
var express = require('express');
```


<b>Http and https:</b> HTTP means HyperText Transfer Protocol. HTTP is the underlying protocol used by the World Wide Web and this protocol defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands. HTTPS means Hypertext Transfer Protocol Secure. Read more

```
var http = require('http');
var https = require('https');
```

<b> Mongoose:</b> Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. It manages relationships between data, provides schema validation, and is used to translate between objects in code and the representation of those objects in MongoDB. Read more

```
var mongoose = require('mongoose');
```


<b>Passport</b> : Passport is authentication middleware for Node.js. Extremely flexible and modular, Passport can be unobtrusively dropped in to any Express-based web application. A comprehensive set of strategies support authentication using a username and password, Facebook, Twitter, and more. Read more

```
var passport = require('passport');    
```


<b>Morgan</b> : Logging middleware for node.js http apps. Read more
  
```
var morgan = require('morgan');
```


<b>Cookie-parser : </b> Parse Cookie header and populate req.cookies with an object keyed by the cookie names. Optionally you may enable signed cookie support by passing a secret string, which assigns req.secret so it may be used by other middleware. Read more

```
var cookieParser = require('cookie-parser');
```

<b>Express-session:</b> HTTP is stateless; in order to associate a request to any other request, you need a way to store user data between HTTP requests. Cookies and URL parameters are both suitable ways to transport data between the client and the server. But they are both readable and on the client side. Sessions solve exactly this problem. You assign the client an ID and it makes all further requests using that ID. Information associated with the client is stored on the server linked to this ID. We put the session and cookie-parser middleware in place. Read more

```
var session = require('express-session');
```

<b> Body parser: </b>  body-parser extract the entire body portion of an incoming request stream and exposes it on req.body . The middleware was a part of Express.js earlier but now you have to install it separately. This body-parser module parses the JSON, buffer, string and URL encoded data submitted using HTTP POST request. Read more

```
var bodyParser = require('body-parser');

```

<b> Filesystem: </b> The Node.js file system module allows you to work with the file system on your computer.The fs module provides an API for interacting with the file system in a manner closely modeled around standard POSIX functions. Read more

```
	var fs = require('fs');
```

<b> Multer: </b> Multer is a node.js middleware for handling multipart/form-data, which is primarily used for uploading files. It is written on top of busboy for maximum efficiency. Read more

```
var multer = require('multer');
````


<b> Favicon:</b>  Node.js middleware for serving a favicon. A favicon is a visual cue that client software, like browsers, use to identify a site. Read more
  
```
var favicon = require('serve-favicon');
```

<b> Busboy: </b> Connect middleware for busboy. Read more
  
```  
var busboy = require('connect-busboy'); //middleware for form/file upload
```

Self designed configuration modules: This includes database configurations and app configuration. 

<b> Database configuration: </b>

Create database configuration variable

```
var configDB = require('./config/database.js');              
```

<b> App configuration: </b>

Create application configuration:
```
var config = require('./config/app.json');
```

<b> MongoDB database connection: </b>

We connect to the MongoDB database with url provided by configDB variable. We follow the strategy required for  mongoose.connect( ): mongoose.connect('mongodb://username:password@host:port/database?options...'); Read more 

```
  			mongoose.connect(configDB.url); // connect to our database
````


<b> Initiate application: </b>

We initiate our express application and implement ‘set’ and ‘use’ methods to specify actions in application.
```
var app = express();
```

<b> Template Engine: </b> A template engine enables you to use static template files in your application. At runtime, the template engine replaces variables in a template file with actual values, and transforms the template into an HTML file sent to the client. This approach makes it easier to design an HTML page. Some popular template engines that work with Express are Pug, Mustache, and EJS. The Express application generator uses Jade as its default, but it also supports several others. Read more

```
app.set('view engine', 'ejs');
app.set('view options', { layout: false });
```

<b> Using Middleware : </b> Express is a routing and middleware web framework that has minimal functionality of its own: An Express application is essentially a series of middleware function calls.Middleware functions are functions that have access to the request object (req), the response object (res), and the next middleware function in the application’s request-response cycle. The next middleware function is commonly denoted by a variable named next. Middleware functions can perform the following tasks:
- Execute any code.
- Make changes to the request and the response objects.
- End the request-response cycle.
- Call the next middleware function in the stack


<b> Static web components: </b>
```
//static site---front end
app.use('/public', express.static('public'));
```


<b> Body parser </b>

```
// body parser
app.use(bodyParser.json());
app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb'}));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(favicon(__dirname + '/public/images/m.ico'));
app.use(busboy()); //to make file upload work
```
<b> Setup express application: </b>
```
		// set up our express application
app.use(morgan('dev')); // log every request to the console
app.use(cookieParser()); // read cookies (needed for auth)
app.use(bodyParser()); // get information from html forms
```
  
<b>Passport setup: </b>
```
app.use(session({ secret: 'migrate' })); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
app.use(flash()); // use connect-flash for flash messages stored in session
```


<b> Routing: </b>
```
require('./routes.js')(app, passport);
```


<b> Run the application </b>

```
var port = config.serverPort; 
app.listen(port);
console.log("server up and running on port " + port);
module.exports = app;

```


