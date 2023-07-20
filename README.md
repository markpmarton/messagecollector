# messagecollector
Sample FastApi containers with Postgres Db


*Please read instructions carefully*

Use this file as part of the README.md and share with us your project when you complete it.

## Requirements

You want to collect stats about the messages your system processes.

For everycustomerId and for everytype of message, you want to know how many messages have been processed and what is the total amount of that specific type for a date interval.

It follows the JSON Schema of the message:

```json
{

"$schema": "https://json-schema.org/draft/2019-09/schema",

"$id": "http://******.com/stats\_message.json",

"type": "object",

"title": "Stats Message Schema",

"required": [

"customerId",

"type",

"amount",

"uuid"

],

"properties": {

"customerId": {

"type": "integer",

"title": "The customerId is the customer unique identifier",

"examples": [

1

]

},

"type": {

"type": "string",

"default": "",

"title": "The type of message received",

"examples": [

"A"

]

},

"amount": {

"type": "string",

"title": "Amount billed to the customer, as a string with 3 decimals precision", "examples": [

"0.012"

]

},

"uuid": {

"type": "string",

"title": "The message unique identifier", "examples": [

"a596b362-08be-419f-8070-9c3055566e7c" ]

}

},

"examples": [{

"customerId": 1,

"type": "A",

"amount": "0.012",

"uuid": "a596b362-08be-419f-8070-9c3055566e7c" }]

}
```

### Instructions

1. Write a REST API that will receive a single message and that updates a statistics table on a relational database.
2. Write a REST API that will provide statistical information back to the reader.

### Hints

- use the *python* programming language, feel free to choose the best framework / libraries to get the task done
- no need to have a fully-working deployed environment, just a local working solution
- write tests
- write comments to facilitate reading for reviewers where code can be unclear
- use *git* and write well formed commit messages
- use of *docker* is appreciated

## Usage

With docker-compose all the required containers will start.
```bash
docker-compose up --build -V
```
The tests can run after the container deploy by running run_tests.sh
