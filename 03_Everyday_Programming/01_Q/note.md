```
정수배열이 아래처럼 있다고 하자.
[a]
[a,b]
[a,b,c]
...

for loop statement에서 index에 의하여 조회되는 current element는 아래와 같다.
index 0 = a
index 1 = b
index 2 = c


for loop statement에서 index에 의하여 조회되는 current element와 이어지는 원소들의 subsequences는 아래와 같다.
[a]
[a,b],   [b]
[a,b,c], [b, c], [c]

for loop statement에서 index에 의하여 조회되는 current element와 이어지는 원소들의 subsequences들의 원소의 합중 제일 큰 것은 아래와 같다.
max(a)
max(a+b, b) = x 라고 하자
max(x+c, c)

for loop statement에서 index와 상관없이 가장 큰 이어지는 원소들의 합을 구하면 아래와 같다.
a
max(a, max(a+b, b)) = y 라고 하자
max(y, max(x+c, c))
```
