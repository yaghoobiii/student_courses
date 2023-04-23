# student_courses

StudentCourses - JavaScript client for student_courses
The API for the Maryam's homework
This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 2.0.0
- Build package: io.swagger.codegen.v3.generators.javascript.JavaScriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install student_courses --save
```

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var StudentCourses = require('student_courses');

var api = new StudentCourses.AuthApi()
var password = "password_example"; // {String} 

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.login(password, callback);
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StudentCourses.AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /login | Login interface for students
*StudentCourses.CourseApi* | [**courseById**](docs/CourseApi.md#courseById) | **GET** /courses/{course_id} | Get a specific course by ID
*StudentCourses.CourseApi* | [**courses**](docs/CourseApi.md#courses) | **GET** /courses | Get all the courses
*StudentCourses.HTMLApi* | [**rootGet**](docs/HTMLApi.md#rootGet) | **GET** / | The main INDEX.html
*StudentCourses.SelectionApi* | [**destroySelection**](docs/SelectionApi.md#destroySelection) | **POST** /selections/destroy | Destroy a selection
*StudentCourses.SelectionApi* | [**insertSelection**](docs/SelectionApi.md#insertSelection) | **POST** /selections/create | Create a selection
*StudentCourses.SelectionApi* | [**selectionByStudent**](docs/SelectionApi.md#selectionByStudent) | **GET** /selections/{student_id} | Get a student&#x27;s selections

## Documentation for Models

 - [StudentCourses.Course](docs/Course.md)
 - [StudentCourses.HTML](docs/HTML.md)
 - [StudentCourses.LoginStatus](docs/LoginStatus.md)
 - [StudentCourses.Selection](docs/Selection.md)
 - [StudentCourses.User](docs/User.md)

## Documentation for Authorization

 All endpoints do not require authorization.
