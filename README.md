# Project Description
This project is a simple Python application that provides an API to return the top n elements of an array. It was built using FastAPI and Python 3.10.

## Prerequisites
1. Python 3.10 or higher
2. Poetry
## Installation
Clone the repository:
```
git clone git@github.com:Element-Ext/offiste-assignment-U3WFQ2P9.git
```
Change into the project directory:
```
cd offiste-assignment-U3WFQ2P9
```
Create a virtual environment:
```
poetry shell
```
Install dependencies with Poetry:
```
poetry install
```
Start the application with Poetry:
```
poetry run uvicorn main:app --reload
```
Navigate to http://localhost:8000/docs in your web browser to view the API documentation.
## Testing
Run the following command in the project directory to execute the tests:
```
poetry run pytest
```


### Assignment
Create a Python web application, using Django or other frameworks, to search for top N elements from an integer array. The application should provide an endpoint to accept requests and respond accordingly. For example, an input of `10,30,20,21,11,22,33,44,15,33,10,30` will yield an output of `44,33,33,30,30` for the top five elements in descending order. The input can be very big. The implementation is expected to handle an array at the size of one million. Please avoid array sorting and be aware of memory usage.

### Requirements
- Follow the standard git practice to,
  - Branch off the main branch
  - Push commits regularly
  - Create a reviewable PR when it's ready, making sure to,
    - Clean up, format, and remove commented code
    - Remove unrelated and auto-generated files
- Design and create an application that can,
  - Process a big input
  - Search for top integers based on the input
  - Handle errors and exceptions
- Write unit tests that,
  - Validate the code logic
  - Handle edge cases which lead to errors and exceptions
- Create README.md that includes,
  - Project description
  - Steps to build and deploy the application locally
  - Test run commands

### Assessments
- Git practice and PR readability
- Architecture, design, logic, and efficiency
- Coding principles
- Documentation and technical writing skills
