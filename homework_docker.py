import requests
import csv
import time

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    return data["iss_position"]["longitude"], data["iss_position"]["latitude"]

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(data)

if __name__ == "__main__":
    csv_filename = "iss_positions.csv"

    while True:
        try:
            longitude, latitude = get_iss_position()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            data = [timestamp, longitude, latitude]

            write_to_csv(csv_filename, data)
            print(f"Data written to {csv_filename}: {data}")

            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)