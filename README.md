# Project Name

## Requirements

- Python 3.12.3
- pip 23.1.2

## Installation

1. Create a virtual environment:

    ```bash
    python3.12 -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate.ps1
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

3. Upgrade pip (if necessary):

    ```bash
    pip install --upgrade pip
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the server

   - On Windows:
  
   ```bash
   py manage.py runserver
   ```
  
   - On Unix or MacOS:

   ```bash
   python3 manage.py runserver
   ```
