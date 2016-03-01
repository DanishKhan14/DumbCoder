def verticalOrder(root):
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)
    for line_no in range(minimum[0], maximum[0]+1):
        printVerticalLine(root, line_no, 0)
        print
def findMinMax(tree, min, max, hd)
     if tree is NULL then return;

     if hd is less than min then
           min = hd;
     else if hd is greater than max then
          max = hd;

     findMinMax(tree->left, min, max, hd-1);
     findMinMax(tree->right, min, max, hd+1);


def printVerticalLine(tree, line_no, hd)
     if tree is NULL then return;

     if hd is equal to line_no, then
           print(tree->data);
     printVerticalLine(tree->left, line_no, hd-1);
     printVerticalLine(tree->right, line_no, hd+1);

def findMinMax(node, minimum, maximum, hd):
    if node is None:
        return
    if hd < minimum[0] :
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    findMinMax(node.left, minimum, maximum, hd-1)
    findMinMax(node.right, minimum, maximum, hd+1)

def printVerticalLine(node, line_no, hd):
    if node is None:
        return
    if hd == line_no:
        print node.data,
    printVerticalLine(node.left, line_no, hd-1)
    printVerticalLine(node.right, line_no, hd+1)