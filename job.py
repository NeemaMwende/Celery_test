# def print_number(lowest, highest):
#     print("==job processing started ==")
#     x = lowest 
#     while x <= highest :
#         print("{}\n".format(x))
#         x = x+1
#     print("==End==")

import logging

logging.basicConfig(level=logging.INFO)

def print_number(lowest, highest):
    logging.info("==job processing started ==")
    x = lowest 
    while x <= highest:
        logging.info("Number: {}", x)
        x = x+1
    logging.info("==End==")
    return list(range(lowest, highest + 1))