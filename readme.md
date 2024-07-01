# ProxyTester

Welcome to ProxyTester. This project is my first real program, and I thought I might as well add it to my repos after finding it on my old computer. 

ProxyTester is a simple tool for testing proxy speeds using various configurations. This README will guide you through the setup, usage, and structure of the project.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configurations](#configurations)

## Introduction

ProxyTester allows you to perform simple speed tests and speed comparison tests on different proxy configurations. The tests will help you evaluate the performance of various proxies by measuring the time it takes to fetch a set of URLs.

## Features

- Simple proxy speed test
- Proxy speed comparison test
- Supports multiple proxy configurations
- Generates CSV reports for comparison tests

## Installation

To get started with ProxyTester, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Hmouaziz/proxytester.git
    ```
2. Change into the project directory:
    ```bash
    cd proxytester
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run ProxyTester, execute the following command:
```bash
python main.py
```

You will be presented with a menu where you can choose to run a simple proxy speed test or a proxy speed comparison test.

### Simple Proxy Speed Test

1. Select "Run simple proxy speed test" from the menu.
2. Choose a proxy configuration to test.
3. Enter the number of URLs you would like to test.
4. The test results will be displayed in the terminal.

### Proxy Speed Comparison Test

1. Select "Run proxy speed comparison test" from the menu.
2. Select at least two proxy configurations for comparison.
3. Enter the number of URLs you would like to test.
4. The test results will be displayed in the terminal.
5. Optionally, you can generate a CSV report of the test results.

## Project Structure

The project is structured as follows:

```
proxytester/
├── Configs/
│   └── geonode_proxy_configs.py  # Contains proxy configurations
├── data/
│   └── random-urls.csv  # Sample URLs for testing
├── functions.py  # Contains helper functions for tests
├── main.py  # Entry point of the application
├── menu.py  # Handles user interface and menu interactions
├── operations.py  # Contains functions for running tests
├── requirements.txt  # Lists required dependencies
└── utils.py  # Contains utility functions like progress bar
```

## Configurations

The proxy configurations are stored in `Configs/geonode_proxy_configs.py`. Here are some sample configurations:

```python
def geonode_US_rotating_residential_unmetered_config():
    username = "geonode_'replace-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "rotating-residential.geonode.com:9000"
    proxy_config = {"http":"http://{}:{}@{}".format(username, password, GEONODE_DNS)}
    return proxy_config
```

Replace the placeholder values with your actual proxy credentials.
