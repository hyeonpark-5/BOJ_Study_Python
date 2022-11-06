import sys

Stack = []
n = int(sys.stdin.readline())

for i in range(n):
     order = sys.stdin.readline().split()
     
     if order[0] == 'push':
          Stack.append(order[1])
     elif order[0] == 'pop':
          if len(Stack) == 0:
               print('-1')
          else:
               print(Stack.pop())     
     elif order[0] == 'size':
          print(len(Stack))
     elif order[0] == 'empty':
          if len(Stack) == 0:
               print('1')
          else:
               print('0')
     elif order[0] == 'top':
          if len(Stack) == 0:
               print('-1')
          else:
               print(Stack[len(Stack)-1])