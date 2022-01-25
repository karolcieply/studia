def check_if_url_is_correct_form(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    return False
