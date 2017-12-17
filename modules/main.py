import utils
from utils import print_matrix as my_print_matrix
from pprint import pprint as pp
import sys


print_matrix = True

utils.print_matrix([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

pp([[1,2,3],
    [4,5,6],
    [7,8,9]])

pp(sys.path)

print("__name__:", __name__)