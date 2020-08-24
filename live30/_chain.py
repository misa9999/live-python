def chain(*iters):
    for l in iters:
        yield from l



# def chain(*iters):
#     for l in iters:
#         for val in l:
#             yield val

