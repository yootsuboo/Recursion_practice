class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp
    
    def pop(self):
        if self.head is None :
            return 
        tmp = self.head
        self.head = self.head.next 
        return tmp.data
    
    def peek(self):
        if self.head is None:
            return
        return self.head.data
        
def isParenthesesValid(parentheses):
    # # ここから書きましょう

    if "})]".find(parentheses[0]) > -1 :
        return False

    stack = Stack()        
    hashmap = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }

    stack.push(parentheses[0])

    for i in range(1,len(parentheses)):
        if "})]".find(parentheses[i]) > -1:
            if stack.peek() == hashmap[parentheses[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.push(parentheses[i])

    return True if stack.peek() == None else False

# def isParenthesesValid(parentheses):

#     charStack = []
#     pairs = {
#         "}":"{",
#         ")":"(",
#         "]":"[",
#     }

#     for i in range(len(parentheses)) :
#         currChar = parentheses[i]

#         if len(charStack) > 0 and currChar in pairs and charStack[-1] == pairs[currChar]: charStack.pop()  
#         else: charStack.append(currChar) 

#     return len(charStack) == 0 

# print(isParenthesesValid("{}")) # true
# print(isParenthesesValid("[{}]")) # true
# print(isParenthesesValid("[{(]")) # false
# print(isParenthesesValid("(){}[]")) # true
# print(isParenthesesValid("((()(())))")) # true
# print(isParenthesesValid("[{(}])")) # false
# print(isParenthesesValid("]][}{({()){}(")) # false
# print(isParenthesesValid("{(([])[])[]}[]")) # true
# print(isParenthesesValid("{(([])[])[]]}")) # false
