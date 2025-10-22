url = input("Enter a URL: ")
if url.startswith("https://"):
    url_without_prefix = url.removeprefix("https://")
else:
    url_without_prefix = url
print("URL without prefix:", url_without_prefix)


