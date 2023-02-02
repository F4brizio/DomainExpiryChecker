# 🔍 Domain Tracker 🕵️
This project is a domain tracker that checks every hour if a domain has expired and has been released using the _ip2whois API_. If the domain has expired, an alert window 🔔 with a message is displayed and a warning 🔊 sound is played.

## Requirements 🧾
- Python 3.x 🐍
- Libraries listed in the requirements.txt file 📚

## Installation 🔧
To install the necessary libraries 📚, run the following command in the terminal 💻:  

```pip install -r requirements.txt ```

## Usage 🚀
To run the script, open a terminal and run the following command:

```python3 tracker.py```

## Configuration 🛠️
You can customize the script configuration by editing the following variables at the beginning of the tracker.py file:

- API_KEY: Your ip2whois API key 🔑.
- DOMAIN: The domain name you want to track 🕵️.

## License 📜
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details