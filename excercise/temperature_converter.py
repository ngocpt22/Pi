temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        with open('result.txt', 'a') as file:
            file.write(str(f) + '\n')
        return "result is written in result.txt file"
for t in temperatures:
    c_to_f(t)

# You should open file one time and then write content in the loop file. See the lecture 71 for more details.