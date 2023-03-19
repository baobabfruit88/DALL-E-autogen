
# DALL-E image generator

This small CLI application written in python uses an API key and Endpoint for DALL-E to generate images either by picking random entries from a given json list. Or by typing a suggestion. 



## Authors

- [@baobabfruit88](https://github.com/baobabfruit88/)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file you can set these manually or through the menu

`API_KEY`

`API_ENDPOINT`

## Suggestions json list 

The list has to be a simple json array i.e (include the []'s in the file) : 

```bash
    ["entry1","entry2","entry3"]
```

## Installation

```bash
    pip3 install -r requirements.txt
    python3 main.py
```
    