# def print_number(lowest, highest):
#     print("==job processing started ==")
#     x = lowest 
#     while x <= highest :
#         print("{}\n".format(x))
#         x = x+1
#     print("==End==")

# job.py - return instead of print
def print_number(lowest, highest):
    result = []
    x = lowest 
    while x <= highest:
        result.append(x)
        x = x+1
    return result