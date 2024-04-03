import requests
import json

def fetch_vendor_data():
    url = 'https://platform.cloud.coveo.com/rest/search/v2'
    headers = {
        'accept': '*/*',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwidG9rZW5JZCI6IndybGpiaTR1a2sycGs3N25kYTR0bWJzYWxhIiwib3JnYW5pemF0aW9uIjoicnNhY3Byb2Q4bXlseTRraiIsInVzZXJJZHMiOlt7InR5cGUiOiJVc2VyIiwibmFtZSI6ImFub255bW91cyIsInByb3ZpZGVyIjoiRW1haWwgU2VjdXJpdHkgUHJvdmlkZXIifV0sInJvbGVzIjpbInF1ZXJ5RXhlY3V0b3IiXSwiaXNzIjoiU2VhcmNoQXBpIiwiZXhwIjoxNzEyMjQ1NzY0LCJpYXQiOjE3MTIxNTkzNjR9.1bUyTCDmUsxBeidAkToRLs_XTlWAZFhEgGbWfhD92FE',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    data = {
        'actionsHistory': '[{"name":"Query","time":"\\"2024-04-03T16:31:53.173Z\\""}]',
        # Add other necessary parameters here
    }

    all_vendor_data = []

    # Initial request to get total number of results
    print("Sending initial request...")
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    total_results = response_data.get('totalCount', 0)
    print(f"Total results: {total_results}")


    # Paginate through results
    page_size = 25
    for start in range(0, total_results, page_size):
        print(f"Fetching results {start} to {start + page_size}...")
        data['firstResult'] = start
        data['numberOfResults'] = page_size

        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        # Extract vendor data and append to the list
        vendor_data = response_data.get('results', [])
        all_vendor_data.extend(vendor_data)

        # Save the current batch of vendor data to the file
        save_to_file(vendor_data, 'filename.json')

    return all_vendor_data

def save_to_file(vendor_data, filename):
    with open(filename, 'w') as f:
        json.dump(vendor_data, f, indent=4)

if __name__ == '__main__':
    all_vendor_data = fetch_vendor_data()
    save_to_file(all_vendor_data, 'vendor_data.json')
    print("Data saved to vendor_data.json")
