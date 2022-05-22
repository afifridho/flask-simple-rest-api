import os

class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400

class Core:
    Timezone = os.getenv('TIMEZONE', 'UTC')