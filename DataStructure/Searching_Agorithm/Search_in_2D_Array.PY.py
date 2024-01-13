# TODO: Question 2:Search in 2D Array-
#  Write an efficient algorithm that searches for a value target in an m x n integer matrix.
#  This matrix has the following properties:
#  Integers in each row are sorted from left to right.
#  The first integer of each row is greater than the last integer of the previous row.
#  If the value is there in the matrix return true, else false.
def search_in_matrix(matrix, target):
   columns = len(matrix[0])
   rows= len(matrix)
   #Binary search to identify the relevent row
   top = 0
   bottom = rows - 1
   while (top<= bottom):
     middle =(top+ bottom)//2
     if target< matrix[middle][0]: bottom = middle -1
     elif target> matrix[middle][columns-1]: top = middle+1
     else : break
   if top > bottom: return False
   left = 0
   right = columns-1
   while( left<= right):
     middle_val = (left+right)//2
     if target == matrix[middle][middle_val]: return True
     elif target < matrix[middle][middle_val]: right = middle_val -1
     else: left = middle_val+1
   return False



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[20,30,40,50]]
print(search_in_matrix(matrix,45))

#TODO: TIME= O(LOG N +LOG M) SPACE= O(1)
