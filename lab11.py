import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth


username = input("Please enter username: ")
password = getpass("Please enter password: ")


authurl = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

token = requests.request("POST", authurl, headers=headers, data=payload)

payload2={}
headers2 = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MTIzZGEzMTdiM2FhOTA2ZWQwYjJiMzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYzNjY1MTYxNiwiaWF0IjoxNjM2NjQ4MDE2LCJqdGkiOiJiNGU5NDljZC00Y2I1LTQyNTktYjBkMi01NTBjNDQwOWQxMzIiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.cn4RRVl2PaM359Y3O7jtH_kDh2VccHNkZuXlXGMzNBGTHIumSpa1lwRv8sUlggtsN3xHC_L548BCuA4I4SGoYmUZghwSC60I-PQsBbfa82NEPr9S4_7IcvMJJ-tYP20WIwbbue-cv2EfATu37NwbJ5EKenKwsfOla6Po1RnOFZ1PyYNDYy5JvMZfSNMmRFKI16OQfqe8PKvWbIKg56qKhFqV3aLg6GzYK125Kk7aJAgAlnpB_oYsOKZopmqlNtLbiPIxSVAokyKiCNiotas9s7Qbh-KKhNYlBHDFTixooqT1rCUte2y--EHR6zQ-5kQQHHqgeIRnd4lLHpZzFLHP0A'
}

list = requests.request("GET", url, headers=headers2, data=payload2)

print(list.text)
