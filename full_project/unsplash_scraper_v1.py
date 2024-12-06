import requests


search_url = "https://unsplash.com/napi/search/photos?page={page}&per_page=20&plus=none&query=happy+person&xp=search-region-awareness%3Aexperiment"
#total_pages = requests.get(search_url).json()["total_pages"]
total_pages = 5

images = []

for page in range(total_pages):
    print(f"scraped pages: {page + 1} - {total_pages}")
    url = search_url.format(page=page + 1)
    response = requests.get(url)
    for image in response.json()["results"]:
        images.append({"url": image["urls"]["small"], "slug": image["slug"]})


for idx, image in enumerate(images):
    print(f"downloading {idx + 1} - {len(images)}")
    response = requests.get(image["url"])
    with open(f"./images/{image["slug"]}", "wb") as f:
        f.write(response.content)
