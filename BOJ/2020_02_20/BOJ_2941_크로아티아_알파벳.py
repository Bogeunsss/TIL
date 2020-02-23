Croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
inputs=input()
for i in Croatia:
    inputs=inputs.replace(i,'0')
print(len(inputs))
