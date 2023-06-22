# Simple XBlock Counter

This is a simple XBlock counter that counts the number of clicks on a button.

## Installation

To install and use the Simple XBlock Counter, follow these steps:

1. Make sure you have Python installed or virtual environment on your system.

2. Follow the instruction below to install and configure Xblock SDK
  ```
    https://github.com/openedx/xblock-sdk
  ```

3. Clone the repository to the xblock-sdk directory:
  ```
    git clone https://github.com/S1mpleOW/counter_xblock.git .
  ```

4. Install the required dependencies:
  ```
    pip install -e counter
  ```

6. Start the XBlock runtime server:
  ```
    python manage.py runserver
  ```

7. Open your web browser and access the XBlock Workbench at `http://localhost:8000/`.

## Usage

Once the Simple XBlock Counter is added to your course, it will display a button. Each time the button is clicked, the counter will increment by one.

## Customization

You can customize the appearance and behavior of the Simple XBlock Counter by modifying the source code. Refer to the documentation and code comments for more information on how to customize the XBlock.
