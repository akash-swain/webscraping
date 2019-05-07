from bs4 import BeautifulSoup
import requests

url = "https://www.nmmc.gov.in/water-bill?p_p_id=onlinewaterpayment_WAR_NMMCProjectportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=1&p_p_col_count=2&_onlinewaterpayment_WAR_NMMCProjectportlet_action=consumerDetails"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

tags = soup.find_all("a")

for tag in tags:
    print (tag.text)