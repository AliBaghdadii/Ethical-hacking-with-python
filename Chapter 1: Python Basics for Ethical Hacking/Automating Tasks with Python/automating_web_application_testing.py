import requests
from bs4 import BeautifulSoup

# A script that automates form submission and checks for basic vulnerabilities:
def submit_form(url, username, password):
    session = requests.Session()

    # Get the login page and extract the CSRF token:
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    # Prepare the form data
    form_data = {
        'username': username,
        'password': password,
        'csrf_token': csrf_token
    }

    # Submit the form
    response = session.post(url, data=form_data)

    return response

def check_vulnerabilities(response):
    vulnerabilities = []

    # Check for SQL injection
    if "SQL syntax" in response.text:
        vulnerabilities.append("Potential SQL Injection vulnerability")

    # Check for XSS
    if "<script>" in response.text:
        vulnerabilities.append("Potential XSS vulnerability")

    # Check for sensitive information exposure
    if "password" in response.text:
        vulnerabilities.append("Potential sensitive information exposure")

    return vulnerabilities

def main():
    url = input("Enter the URL of the login page: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    response = submit_form(url, username, password)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    vulnerabilities = check_vulnerabilities(response)

    if vulnerabilities:
        print("Potential vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"- {vuln}")
    else:
        print("No obvious vulnerabilities found.")

if __name__ == "__main__":
    main()