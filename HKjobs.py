import requests
import json
import csv

def write_to_csv(entries, filename):
    keys = entries[0].keys() if entries else []
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(entries)

all_entries = []

#job "1" = full time, "2" = part time, "3" = internship, "4" = temporary

for x in range(1, 50):
    url = 'https://job.heykorean.com/api/job/list?limit=20&page='
    url2 = '4&sorting=1&area_code=4478&job_type=2'
# AREA CODES #
#4480 NEW YORK
#4478 NEW JERSEY

  
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url + str(x) + url2, headers=headers)

    if response.status_code == 200:
        data = response.json()

        entries = data['list']
        for entry in entries:
            listing_id = entry.get("id")
            listing_link = f"https://job.heykorean.com/job/view/{listing_id}" if listing_id else "No Link"
            company_id = entry.get("company_id")
            listing_company =f"https://job.heykorean.com/job/view/{company_id}" if company_id else "None"

            entry_data = {
                "Job": entry.get("title"),
                "Sponsor?": entry.get("sponsor_visa"),
                "Remote?": entry.get("remote_work"),
                "Open?": entry.get("status"),
                "Views": entry.get("count_view"),
                "Link:": listing_link,
                "Ending_Date": entry.get("perioid_end"),
                "Company": entry.get("company_name"),
                "C_Link": company_id,
                "C_About": entry.get("company_about_us_line")
            }


            all_entries.append(entry_data)
            print(entry_data)
    else: print("resp error")

csv_filename = 'HK.JOB.csv'

write_to_csv(all_entries, csv_filename)
print(f"Data has been written to {csv_filename}")
