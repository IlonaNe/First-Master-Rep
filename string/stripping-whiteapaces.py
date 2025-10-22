text_with_whitespaces = "   Hello, World!   \n\t"
#enter_text_with_whitespaces = input("Enter text with whitespaces: ")
text_without_whitespaces_from_left = text_with_whitespaces.lstrip()
text_without_whitespaces_from_right = text_with_whitespaces.rstrip()
text_without_whitespaces = text_with_whitespaces.strip()
print(f"Original text: '{text_with_whitespaces}'")
print(f"Text without leading whitespaces: '{text_without_whitespaces_from_left}'")
print(f"Text without trailing whitespaces: '{text_without_whitespaces_from_right}'")
print(f"Text without leading and trailing whitespaces: '{text_without_whitespaces}'")