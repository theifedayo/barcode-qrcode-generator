# Barcode-QRcode-Generator

<center>
    <img width="509" alt="Screenshot 2022-08-31 at 16 37 20" src="https://user-images.githubusercontent.com/47679952/187741025-1926fb56-e2cb-42c7-90a2-f0c87105f4b9.png"/>


<p float="left">
    <img width="389" alt="Screenshot 2022-08-31 at 16 39 09" src="https://user-images.githubusercontent.com/47679952/187741430-e1cd5938-97c5-4d47-a090-2ce501e28585.png"/>
    <img width="389" alt="Screenshot 2022-08-31 at 16 39 18" src="https://user-images.githubusercontent.com/47679952/187743339-0bf68d2a-1736-4567-b038-702c5630a27d.png"/>

</p>

<p float="left">
    <img width="389" alt="Screenshot 2022-08-31 at 16 39 36" src="https://user-images.githubusercontent.com/47679952/187743286-3258135b-f37f-4926-a190-c403fbbdd04e.png"/>
    <img width="389" alt="Screenshot 2022-08-31 at 16 39 50" src="https://user-images.githubusercontent.com/47679952/187743426-7a2e058b-e8a1-43b2-8aa7-d0e8713f7bca.png"/>  
    </p>
</center>


## Introduction

This is a webapp that generates bar and qr code. It takes in user's content and generates bar and qr code as png and svg format.

## Requirements

* [Python](https://python.org) -  v3.7 above
* [Virtualenv](https://pypi.org/project/virtualenv/) - v20.12.0 above

## Installation and Usage
 Clone this repo

  ```bash
  git clone https://github.com/theifedayo/barcode-qrcode-generator.git
  ```
Change directory
```bash
  cd barcode-qrcode-generator
  ```
Create virtual environment
```bash
  python3.8 -m venv env
  ```
Activate your virtual environment
```bash
  source env/bin/activate
  ```
Install requirements
```bash
  pip install -r requirements.txt
  ```
Run the server

  ```bash
  python manage.py runserver
  ```
Screenshots above should help in the app usage

## Contribution
Fork this repo and add exciting feature. If I don't get too much backlog at work, I'll add svg-as-code support on webpage instead of downloading before seeing the svg code
