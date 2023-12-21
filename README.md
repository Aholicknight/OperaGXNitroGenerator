# Opera GX Nitro Generator

This python script generates nitro gifts from the [Opera GX promotion](https://www.opera.com/gx/discord-nitro) that runs till July 16, 2024.

## What does this python script do?

This Python script is designed to send a series of POST requests to a specific URL and record the responses. Here's a step-by-step breakdown of its functionality:

1. The script starts by importing necessary modules and initializing colorama, a module used for colored console output.

2. It then asks the user to input the number of requests they would like to make.

3. The script clears the console and prepares to send the requests.

4. For each request, the script generates a new UUID and sends a POST request to the specified URL with the UUID as part of the request data.

5. If the response status code is 200 (indicating a successful request), the script checks for a 'token' in the response data. If a token is found, the script increments a counter of successful requests and writes a link containing the token to a file named 'generatedcodes.txt'.

6. If the response status code is 429, the script informs the user that they are being rate-limited. If the status code is anything else, the script informs the user that the request failed.

7. While the requests are being made, the script displays an animation in the console and updates the console title with the number of successful requests.

8. Once all requests have been made, the script clears the console and displays a final message indicating the number of successful requests.

9. The script then waits for the user to press any key before exiting.

## Requirements

To use the python script, you need to run:

```
pip install requests colorama
```

or install via requirements.txt

## Usage

1. After installing the requirements, open a terminal where you have the python script and run `python generator.py`

2. The python script will ask how many gift links you would like to generate (example: 5)

3. The python script will generate the 5 links into the file `generatedcodes.txt`

4. After generating, the console will be cleared and say "Successfully generated (number of generated codes here)!" and ask press any key to close.