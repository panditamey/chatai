# huggingChat
A Python api to use the huggingChat service

# exemple
You can create a chatbot in the terminal with this code:
```python
import sys

hc = HuggingChat()

while True:
    inp = str(input("> "))
    c = hc.chat(inp)
    for i in c:
        char = i["token"]["text"]
        if char == "</s>":
            sys.stdout.write("\n")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
```
