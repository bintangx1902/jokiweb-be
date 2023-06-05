def get_template(temp: str):
    return f"certif/{temp}.html"


def find_data(model, nim, type):
    data = model.objects.filter(nim=nim, type=type)
    return True if data else False
