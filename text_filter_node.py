import re

class TextFilter:
    CATEGORY = "Roblox"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "keywords": ("STRING", {"default": ""}),
                "replace": ("STRING", {"default": ""}),
                "match_case": ("BOOLEAN", {"default": False}),
                "remove_extra_spaces": ("BOOLEAN", {"default": False}),
                "remove_trailing_punctuation": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result_text",)
    FUNCTION = "filter_text"

    def filter_text(self, text, keywords, replace, match_case, remove_extra_spaces, remove_trailing_punctuation):
        # Convert keywords string to a list of words
        keywords_list = [word.strip() for word in keywords.split(",") if word.strip()]

        # If replace is empty, set it to an empty string to remove keywords from text
        if replace == "":
            replace = ""

        # Replace or remove keywords
        for keyword in keywords_list:
            if not match_case:
                # Case insensitive replacement using regex
                pattern = re.compile(re.escape(keyword), re.IGNORECASE)
                text = pattern.sub(replace, text)
            else:
                # Case sensitive replacement
                text = text.replace(keyword, replace)

        # Remove extra spaces and clean punctuation if enabled
        if remove_extra_spaces:
            # Replace multiple spaces with a single space
            text = re.sub(r'\s{2,}', ' ', text)
            # Remove spaces before punctuation marks
            text = re.sub(r'\s+([!:.,?])', r'\1', text)
            # Remove multiple consecutive commas
            text = re.sub(r',+', ',', text)
            # Trim spaces at the end of the text
            text = text.strip()

        # Remove trailing punctuation at the end of the process if enabled
        if remove_trailing_punctuation:
            text = re.sub(r'[!:.,?]$', '', text)

        return (text,)
