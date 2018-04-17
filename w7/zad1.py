def flatten_gen(element):
    for e in element:
        if isinstance(e, list):
            for e_elem in flatten_gen(e):
                yield e_elem
        else:
            yield e
            
def flatten(list_to_change):
    return list(flatten_gen(list_to_change))