import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

GOAL_PRICE = 300

LINK = 'https://www.amazon.ca/gp/aw/d/B0CHWRXH8B/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=0642153153d0dc1e8bb64b09802e9178&hsa_cr_id=8697153580001&qid=1727993270&sr=1-2-9e67e56a-6f64-441f-a281-df67fc737124&ref_=sbx_be_s_sparkle_lsi4d_asin_1_title&pd_rd_w=CZp5a&content-id=amzn1.sym.b63e1afd-fa7d-4ee5-8745-6f3b9e8da6bd%3Aamzn1.sym.b63e1afd-fa7d-4ee5-8745-6f3b9e8da6bd&pf_rd_p=b63e1afd-fa7d-4ee5-8745-6f3b9e8da6bd&pf_rd_r=J5X7HMG1EVN65Z2THXXQ&pd_rd_wg=8IE34&pd_rd_r=1ae8fb69-0462-4634-8278-48c388c564fb'

response = requests.get(url=LINK, headers={"Accept-Language":"en-US", "sec-ch-ua-platform":"macOS"})
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = soup.find(name="span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")


price_float = float(price.text.split("$")[-1])


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = 587

if price_float < GOAL_PRICE:
    with smtplib.SMTP(host=f"{SMTP}", port=PORT) as mail:
        mail.starttls()
        mail.login(user=EMAIL, password=PASSWORD)
        mail.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Price Drop Alert!{price_float} \n\n"
                                                           f"You can get the item at the price you wanted\n\n"
                                                           f"Click the link: {LINK}\n\n"
                                                           f"Chaw Chaw\n"
                                                           f"CyberDude")