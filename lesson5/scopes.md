Python variables scopes
----------------------------

1. Builtin -> lives till the end of runtime

    sum, zip, ValueError, list, dict...

2. Module -> lives till the end of file

    everything above the current interpreter position in the current file + imports

3. Function -> lives till the end of func
   
    everything declared in the function + arguments

4. Function in function...
