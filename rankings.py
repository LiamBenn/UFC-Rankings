#!/home/liam/python/ufcstats/bin
import requests
import re
import sys
from bs4 import BeautifulSoup as bs

# Setup
url = requests.get("https://www.itnwwe.com/mma/ufc-rankings/")
soup = bs(url.text, 'html.parser')


def rankings(element):
    # CSS Selector As Element
    elem = soup.select(element)
    content = elem[0].text
    content = content.replace("(", " ")
    content = content.replace(")", " ")
    # Find Pattern
    pattern = re.compile(r"(?:Champion:|\d+\.)\s+\w+\s\w+\s+\d+-\d+-\d+")
    matches = pattern.findall(content)
    fighter_ranks = '\n'.join(matches)

    return fighter_ranks


# Assign Weight Classes, (m)en & (w)omen
weight_class_rankings = {
    "m_p4p": rankings(".kadence-column_b8bbf4-03 > div:nth-child(1)"),
    "m_heavyweight": rankings(".kt-svg-icon-list-items_68bb27-ed > ul:nth-child(1)"),
    "m_light_heavyweight": rankings(".kt-svg-icon-list-items_659b4f-00 > ul:nth-child(1)"),
    "m_middleweight": rankings(".kt-svg-icon-list-items_2743c7-33 > ul:nth-child(1)"),
    "m_welterweight": rankings(".kt-svg-icon-list-items_82cd81-fc > ul:nth-child(1)"),
    "m_lightweight": rankings(".kt-svg-icon-list-items_00ea45-f0 > ul:nth-child(1)"),
    "m_featherweight": rankings(".kt-svg-icon-list-items_91412b-2d > ul:nth-child(1)"),
    "m_bantamweight": rankings(".kt-svg-icon-list-items_195a09-5b > ul:nth-child(1)"),
    "m_flyweight": rankings(".kt-svg-icon-list-items_62f802-5b > ul:nth-child(1)"),
    "w_p4p": rankings(".kadence-column_82ab3b-c7 > div:nth-child(1) > div:nth-child(3)"),
    "w_bantamweight": rankings(".kt-svg-icon-list-items_1c7b33-e3 > ul:nth-child(1)"),
    "w_flyweight": rankings(".kt-svg-icon-list-items_1400c1-04 > ul:nth-child(1)"),
    "w_strawweight": rankings(".kt-svg-icon-list-items_acf1a0-3a > ul:nth-child(1)")
    }

weight_class_names = [
    "m_p4p",
    "m_heavyweight",
    "m_light_heavyweight",
    "m_middleweight",
    "m_welterweight",
    "m_lightweight",
    "m_featherweight",
    "m_bantamweight",
    "m_flyweight",
    "w_p4p",
    "w_bantamweight",
    "w_flyweight",
    "w_strawweight"
]

error_message = "Weight Class Does Not Exist! Please Try Again or press CTRL+C to quit. "

introduction = """
To see all rankings type 'all'

Pound for Pound = m_p4p
Heavyweight = m_heavyweight
Light Heavyweight = m_light_heavyweight
Middleweight = m_middleweight
Welterweight = m_welterweight
Lightweight = m_lightweight
Featherweight = m_featherweight
Bantamweight = m_bantamweight
Flyweight = m_flyweight
Womens Pound for Pound = w_p4p
Womens Bantamweight = w_bantamweight
Womens Flyweight = w_flyweight
Womens Strawweight = w_strawweight \n"""

try:
    if sys.argv[1].lower() == "all":
        for i in weight_class_names:
            print(f"\n{weight_class_rankings[i]}\n")
    else:        
        print(f"\n{weight_class_rankings[sys.argv[1]]}\n")
except KeyError:
    print(error_message)
except IndexError:
    print(introduction)
    v = input("Please Enter A Weight Class: ")
    try:
        if v.lower() == "all":
            for i in weight_class_names:
                print(f"\n{weight_class_rankings[i]}\n")
        else:
            print(f"\n{weight_class_rankings[v]}\n")
    except KeyError:
        print(error_message)
