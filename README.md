# graphql-layer

# How to install dependencies
pip install -r requirements.txt

# How to run tests
pytest ./tests

# How to run server
uvicorn main:app
# For Development add reload option
uvicorn main:app --reload

# How to test GraphQL Layer
 1. Run Server
 2. Navigate to /graphql endpoint

 3a. Run a query of similar composition to the below example
q uery {
    getOneMessage(args) {
        body
    }
}

# 3b. Run a mutation of similar composition to the below example
mutation {
    addOneCustomer(args) {
        firstName
        lastName
        phone
    }
}