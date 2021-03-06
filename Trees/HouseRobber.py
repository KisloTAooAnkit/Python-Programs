

class Item:
    def __init__(self,withRob,withoutRob) -> None:
        self.withoutRob = withoutRob
        self.withRob = withRob



def helper(root) -> Item:
    if not root:
        return Item(0,0)
    
    left = helper(root)
    right = helper(root)

    #hamne root ko chori kiya
    withRob = root.val + left.withoutRob + right.withoutRob
    #hamne root ko ignore kia
    withoutRob = max(left.withRob,left.withoutRob) + max(right.withRob,right.withoutRob)

    return Item(withRob,withoutRob)




