from flask import Blueprint, jsonify
from .scrapper import scrape_doctors

routes = Blueprint('routes', __name__)

URLS = [
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQU5BIn0.4mn-CHZtv1Ger_2L_jonfDcnADP8Va4GzfQ_NNeZwVU",
            "type": "Dokter Spesialis Anak"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQU5UIn0.q_Rg12NeKiR3tcSw2Qd-3beL2ttm5dsiLNFJxOzBA5k",
            "type": "Dokter Spesialis Anastesi"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiQkVEIn0.ohdLEPnqtGCsd0atK_F5jWfz1sqnRO8G1FSCykkHvlU",
            "type": "Dokter Spesialis Bedah"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiR0lHIn0._fQGxUAOsuys5Iu_xZJuuPQtKS2zr6I1WBFOhyyJkiw",
            "type": "Dokter Spesialis Gigi dan Mulut"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiSU5UIn0.KwMKBvDub6dV5jHrGj_WaBZ8D22Ny2otsKNIs4a7hiY",
            "type": "Dokter Spesialis Penyakit Dalam"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiS0xUIn0.qvPnfHw0h5CEQ2izgUOrKgisREcH1wlB1SE0KC6vChg",
            "type": "Dokter Spesialis Kulit dan Kelamin"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiTUFUIn0.yckN3KwDN9abT6gstg9lI8Z4P5PoiVuoz5dQz5D4UVE",
            "type": "Dokter Spesialis Mata"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiT0JHIn0.knHD2ybbhDNXG5vkciQcRYVkCJknDByUSKlm0iQXdIw",
            "type": "Dokter Spesialis Kandungan"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUEFLIn0.TaSkLk2QTXMOPfmFCKvjsAoqyUhISZrc-pgAnrVmyLA",
            "type": "Dokter Spesialis Patologi Klinik"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUEFSIn0.3UtGzb_b9XBDQB5UCbc-w8YEkZ86_a-t7f_myKw8uMg",
            "type": "Dokter Spesialis Paru"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiUkRPIn0.fAu37NlT_AD2hmqn4dRY9ENg5UqVqE3BOZlp1RHgkto",
            "type": "Dokter Spesialis Radiologi"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiU0FSIn0.SgiVnpAcTSvBnLURNES9kbpEOCSLBzRR7-cN_vScbm8",
            "type": "Dokter Spesialis Saraf"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiVEhUIn0.DzQOKuOe9IjRS3a-NrwU200vW9_k1TFJcwPSXuE5t5w",
            "type": "Dokter Spesialis THT-KL"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTAxIn0.VncL-YgcepzuzZal-zEusOZvaq5r89TdLJWi3q7Xhus",
            "type": "Dokter Spesialis Psikologi"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTcwNzQ0NDMxMCJ9.JShbr-XctB8NoCjokSBs6iDEEou_kuW0EGT3xwr3X5g",
            "type": "Dokter Spesialis Konservasi Gigi"
        },
        {
            "url": "https://rsaqidah.com/dokter/dokter-spesialis/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrb2RlIjoiMTcxNDk3Mjg5MiJ9.Ig6c5B4cXqRHivDA8zHUoa4XTVJHEhgHAK5J5UasThg",
            "type": "Dokter Spesialis Kedokteran Jiwa"
        },
    ]

@routes.route('/doctors', methods=['GET'])
def get_all_doctors():
    all_doctors = []
    for entry in URLS:
        doctors = scrape_doctors(entry["url"], entry["type"])
        all_doctors.extend(doctors)

    return jsonify({
        "error": False,
        "message": "Success",
        "data": all_doctors
    })
