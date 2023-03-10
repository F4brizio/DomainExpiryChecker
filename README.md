# ๐ Domain Tracker ๐ต๏ธ
This project is a domain tracker that checks every hour if a domain has expired and has been released using the _ip2whois API_. If the domain has expired, an alert window ๐ with a message is displayed and a warning ๐ sound is played.

## Requirements ๐งพ
- Python 3.x ๐
- Libraries listed in the requirements.txt file ๐

## Installation ๐ง
To install the necessary libraries ๐, run the following command in the terminal ๐ป:  

```pip install -r requirements.txt ```

## Usage ๐
To run the script, open a terminal and run the following command:

```python3 tracker.py```

## Configuration ๐ ๏ธ
You can customize the script configuration by editing the following variables at the beginning of the tracker.py file:

- API_KEY: Your ip2whois API key ๐.
- DOMAIN: The domain name you want to track ๐ต๏ธ.

## License ๐
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details