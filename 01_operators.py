"""
## Operators in Python (complete list + examples)

### 1) Arithmetic operators
- `+` add: `a + b`
- `-` subtract: `a - b`
- `*` multiply: `a * b`
- `/` true division: `a / b`
- `//` floor division: `a // b`
- `%` modulo (remainder): `a % b`
- `**` exponent: `a ** b`

### 2) Comparison (relational) operators
Return `True/False`
- `==` equal: `a == b`
- `!=` not equal: `a != b`
- `>` greater than: `a > b`
- `<` less than: `a < b`
- `>=` greater or equal: `a >= b`
- `<=` less or equal: `a <= b`

### 3) Assignment operators
Assign a value to a variable
- `=` simple: `x = 5`
- `+=` add-assign: `x += 2`
- `-=` sub-assign: `x -= 2`
- `*=` mul-assign: `x *= 2`
- `/=` div-assign: `x /= 2`
- `//=` floor-div-assign: `x //= 2`
- `%=` mod-assign: `x %= 2`
- `**=` exponent-assign: `x **= 2`

### 4) Logical operators
Combine boolean expressions
- `and` : `a and b`
- `or` : `a or b`
- `not` : `not a`

### 5) Bitwise operators (for integers)
Operate on bits
- `&` AND: `a & b`
- `|` OR: `a | b`
- `^` XOR: `a ^ b`
- `~` NOT: `~a`
- `<<` left shift: `a << 2`
- `>>` right shift: `a >> 2`

### 6) Membership operators
Check existence in a container
- `in` : `x in seq`
- `not in` : `x not in seq`

### 7) Identity operators
Check whether two references point to the same object
- `is` : `a is b`
- `is not` : `a is not b`

### 8) Special operators
- `()` function call: `f(x)`
- `[]` indexing/slicing: `a[0]`, `a[1:3]`
- `.` attribute access: `obj.name`
- `,` tuple packing: `x = (1, 2)`

### 9) The walrus operator (Python 3.8+)
- `:=` assign-expression: `if (n := len(s)) > 0: ...`

---

If you want, I can also list them **in order of precedence** (which operators run first).


"""
a="Rizwan"
b="Mehmood"
print(a+b)  #concatenation
# print(a-b)   not possible str-str


x=10
y=20

x=y
print(y)  #20