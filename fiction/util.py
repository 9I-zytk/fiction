def remove_space(string):
    return "".join(string.split(" "))


def get_source_id(string):
    name = string.split('.com')[1]
    return name.split('/')[1]
