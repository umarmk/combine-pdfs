import requests
import os

def test_merge():
    url = 'http://127.0.0.1:5000/merge'
    files = {
        'file1': open('test1.pdf', 'rb'),
        'file2': open('test2.pdf', 'rb')
    }
    data = {'filename': 'backend_test_merged'}
    
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        with open('backend_test_merged.pdf', 'wb') as f:
            f.write(response.content)
        print("Merge successful! File saved as backend_test_merged.pdf")
    else:
        print(f"Merge failed with status code: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    test_merge()
