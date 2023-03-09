# monkey patch on python
```
modifies other code at runtime (typically at startup).
```

# example
```
from SomeOtherProduct.SomeModule import SomeClass

def speak(self):
    return "ook ook eee eee eee!"

SomeClass.speak = speak
```
