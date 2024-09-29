import requests
import os
base_url = "https://www.pearsonactivelearn.com/r00/r0071/r007180/r00718092/current/OPS/images/POLITICS_GCE_7020_refinary_combined-"
os.makedirs("./pictures", exist_ok=True)
for i in range(1, 618):
    image_url = base_url + str(i).zfill(3) + ".jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"./pictures/image_{str(i).zfill(3)}.jpg", "wb") as file:
            file.write(response.content)
            print(f"Image {str(i).zfill(3)} downloaded successfully.")
    else:
        print(f"Failed to download image {str(i).zfill(3)}.")

print("All images downloaded.")