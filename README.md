# Userinyerface Testing

## Description

### This project is designed for automated testing of key Userinyerface pages:

- Cards
- Help form
- Cookie form
- Main form

## Installation

### Clone the repository:

```bash
    git clone https://github.com/tquality-education/r.ayupov.git
``` 

### Go to the project folder:

```bash
    cd r.ayupov
``` 

### Deploy a virtual environment:

```bash
    python -m venv venv
``` 

### Enable a virtual environment:

<details>
  <summary>Windows</summary>

```bash
    venv\Scripts\activate.bat
``` 

</details>
<details>
  <summary>Linux & MacOS</summary>

```bash
    source venv/bin/activate
``` 

</details>

### Install the dependencies:

```bash
    pip install -r requirements.txt
``` 

## Running the Tests

### Basic Run

```bash
    pytest
``` 
### Run tests by groups

Tests are organized in the tests folder with subfolders:

__units__ — unit tests

__scenarios__ — scenario/integration tests

You can run tests from a specific folder, for example:

```bash
    pytest tests/units
``` 
or
```bash
    pytest tests/scenarios
```
to run only unit or scenario tests respectively.

## Locale and Dialog Configuration
The system locale is detected automatically to handle OS dialogs during file uploads.

You need to add dialog window titles and button names for your locale in the configuration file test_data.json following this pattern:
```json
{
  "os_language": {
    "ru": {
      "dialog_title": "Открытие",
      "edit": "Edit",
      "open_button": "Открыть"
    },
    "en": {
      "dialog_title": "Open",
      "edit": "Edit",
      "open_button": "Open"
    }
  }
}