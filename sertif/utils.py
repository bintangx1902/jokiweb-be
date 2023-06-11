import string, random


def get_template(temp: str):
    return f"certif/{temp}.html"


def find_data(model, nim, type):
    data = model.objects.filter(nim=nim, type=type)
    return True if data else False


def create_slug(n):
    letters = string.ascii_letters
    num = '1234567890'
    raw = letters + num
    return ''.join(random.sample(raw, n))