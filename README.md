# Learnbeat - API client example
This repo contains an example API client that can be used for interacting with the publicly available Learnbeat routes.
Each non-empty JSON response is automatically saved in the `/responses` table with the current timestamp as filename.
Feel free to edit the files and structure to your preferences. They are merely intended as a stepping stone.
For example, automatically storing the response in a `Pandas` dataframe or a different file-format. 
For more in-depth explanation on the API, please take a look at the provided API documentation. 
I would advise opening the .yaml file in an OpenAPI editor like [Swagger](https://editor.swagger.io).

Make sure to set the following settings to get started:
+ Set the `token` variable in `api.py` to one of the provided tokens
+ Set the `HOST` environment variable to the provided url
+ Have fun!

![Learnbeat logo](https://learnbeat.nl/wp-content/uploads/sites/12/2017/09/site-logo.png)