# -*- coding: utf-8 -*-
#!/usr/bin/env python
from subprocess import Popen, PIPE, STDOUT


input = "Hello World. 中文斷詞"
p = Popen(['java', '-jar', 'Tokenizer.jar'], stdout=PIPE, stdin=PIPE)
out = p.communicate(input=input)[0]
print(out)
