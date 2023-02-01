# tech201_control_flows


## Control Flow

- Control flow is way to allow a program to make decisions
  with some built in tools such as the `if`, `elif` or `else`.

### If statement

- This is one of the control flow statements used to help the
  the program make a decision. First we put the `if` statement 
  followed by a statement such as `age > 18` or `film_rating == "Universal""`.
  We then follow it with a `:` and output of our choice.

### Elif / else statements

- `elif` is used when there are multiple decision that can be made so we can put
  them all in the same code block. `Else` is used of none of the decision blocks
  are hit.


## For Loop

`list_data = [1, 2, 3, 4, 5]`

`for num in list_data:
    print(num * 2)`
    
## While Loop

`num = 1


while num <= 100:
    if (num % 3) == 0 and (num % 5) == 0:
        print("FizzBuzz")
        num += 1
    elif (num % 3) == 0:
        print("Fizz")
        num += 1
    elif (num % 5) == 0:
        print("Buzz")
        num += 1
    else:
        print(num)
        num += 1`
