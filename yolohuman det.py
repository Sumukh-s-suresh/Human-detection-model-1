from openimages.download import download_images

# Specify the directory where you want to save the images
output_directory = "./openimages"

# Define the label (e.g., "Scissors")
label = "Scissors"

# Provide the path to your exclusions file
#exclusions_file = "/path/to/exclusions.txt"

# Set the limit for the number of images to download (e.g., 100)
limit = 100

# Download the images, excluding those listed in the exclusions file
download_images(output_directory, [label], limit=limit)
