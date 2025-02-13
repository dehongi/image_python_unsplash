import requests

# Replace with your Unsplash API key
access_key = "YOUR_UNSPLASH_ACCESS_KEY"
query = "mountain"  # Your search query

url = f"https://api.unsplash.com/photos/random?query={query}&client_id={access_key}&count=1"

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data:
        # Get the image URL
        image_url = data[0]["urls"]["regular"]
        print(f"Image URL: {image_url}")

        # Send a GET request to the image URL to download it
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            # Save the image to a local file
            with open("downloaded_image.jpg", "wb") as f:
                f.write(image_response.content)
            print("Image downloaded successfully!")
        else:
            print("Failed to download the image.")
    else:
        print("No image found for the query.")
else:
    print(
        f"Failed to fetch data from Unsplash API. Status code: {response.status_code}"
    )
