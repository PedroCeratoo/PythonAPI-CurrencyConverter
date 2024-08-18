# Currency Converter

## Overview

The **Currency Converter** is a Python application designed to allow users to convert between different currencies in real-time using a modern graphical user interface (GUI). The application reads available currencies and their conversion possibilities from XML files, retrieves current exchange rates via an API, and provides a seamless conversion experience.

## Features

- **Dynamic Currency Selection**: Automatically loads available currencies and updates the conversion options based on the user's selection.
- **Real-time Conversion**: Uses live exchange rates fetched from a trusted API to provide accurate conversion results.
- **Modern GUI**: A user-friendly interface built with `customtkinter`, featuring a dark theme for better visual comfort.

## Installation

### Prerequisites

Make sure you have Python installed on your machine. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Required Libraries

The following Python libraries are required to run this application:

- `customtkinter`: For creating the modern graphical user interface.
- `xmltodict`: For parsing XML files that contain currency data.
- `requests`: For making API requests to retrieve current exchange rates.

You can install these libraries using `pip`:

```bash
pip install customtkinter xmltodict requests
