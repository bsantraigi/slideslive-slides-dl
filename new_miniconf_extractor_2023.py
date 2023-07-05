import os
import json
import requests
import argparse

def download_images_from_json(json_path):
    # Extract id from input file name
    file_name = os.path.basename(json_path)
    id = os.path.splitext(file_name)[0]

    # Load JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Create directory if it doesn't exist
    output_dir = id
    os.makedirs(output_dir, exist_ok=True)

    # Download images
    for index, slide in enumerate(data['slides']):
        image_name = slide['image']['name']
        image_ext = slide['image']['extname']
        download_url = f"https://d1qcbvwoy8vxsg.cloudfront.net/{id}/slides/{image_name}.png?h=720&f=webp&s=lambda&accelerate_s3=1"
        file_name = f"{index + 1:03}_{image_name}{image_ext}"
        file_path = os.path.join(output_dir, file_name)

        # Send HTTP request and save the file
        response = requests.get(download_url)
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded {file_name}")

    print("All images downloaded successfully!")

# Create an argument parser
parser = argparse.ArgumentParser(description='Download image files from a JSON file')
parser.add_argument('json_file', help='path to the JSON file')

# Parse the command-line arguments
args = parser.parse_args()

# Call the download_images_from_json function with the JSON file path
download_images_from_json(args.json_file)

