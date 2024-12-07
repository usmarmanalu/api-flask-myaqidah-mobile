import requests
from bs4 import BeautifulSoup

def scrape_doctors(url, doctor_type):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    doctors = []

    for doctor_div in soup.find_all("div", class_="card"):
        img_tag = doctor_div.find("img")
        image = img_tag["src"] if img_tag else "Image tidak tersedia"
        name_tag = doctor_div.find("h6")
        name = name_tag.text.strip() if name_tag else "Nama tidak tersedia"
        
        schedule_table = doctor_div.find_next("table")
        schedule = []

        if schedule_table:
            for row in schedule_table.find_all("tr")[1:]:
                day = row.find("th").text.strip()
                time = [td.text.strip() for td in row.find_all("td") if td.text.strip() != "- - -"]
                if time:
                    schedule.append(f"{day}: {', '.join(time)}")

        doctors.append({
            "image": image,
            "name": name,
            "schedule": "\n".join(schedule) if schedule else "Jadwal tidak tersedia",
            "type": doctor_type
        })
    return doctors
