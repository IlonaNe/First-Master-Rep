url = input("Enter a URL: ")
suffix_to_remove = input("Enter the suffix to remove: ")
if url.endswith(suffix_to_remove):
    url_without_suffix = url.removesuffix(suffix_to_remove)
else:
    url_without_suffix = url
print("URL without suffix:", url_without_suffix)    