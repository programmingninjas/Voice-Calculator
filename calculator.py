import math
from numerizer import numerize


def calculate(input):

    def multiply(*args):

        for i in args:

            if i == args[0]:

                product = 1

            product = i * product

        return product

    def divide(a, b):

        try:

            division = a/b

            return division

        except:

            print('error')

    def factorial(n, x=None):

        try:

            return math.factorial(n)

        except:

            print('Number should be a whole number')

    def subtract(a, b):

        return a-b

    def power(base, raised):

        return math.pow(base, raised)

    def log(x, base=None):

        try:
            try:
                return math.log(x, base)
            except:
                return math.log(x)

        except:
            print('undefined')

    def square_root(x, n=None):

        try:

            return math.sqrt(x)

        except:
            print('square root of a negative number is not defined')


    string = input[:len(input)-1] if input[-1] == '.' else input

    string = string.replace(',','')

    text0 = (string.lower()).split()

    print(text0)

    values = []

    numerals = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','billion','million','hundred','thousand']

    for num in numerals:              #converting numerals if present into digits

        if num in text0:

            for i in range(len(text0)):

                try:
                    if not text0[i].isdigit():

                        text0[i] = numerize(text0[i])
                        print(text0)
                except:
                    pass

    try:

        global text

        if 'add' in input.lower() or '+' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: '+ str(sum(values))
            

        if 'subtract' in input.lower() or '--' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: '+ str(subtract(values[0], values[1]))

        if 'multiply' in input.lower() or '*' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: ' + str(multiply(*values))

        if 'divide' in input.lower() or '/' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: ' + str(divide(values[0], values[1]))


        if 'raised' in input.lower() or 'power' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: ' + str(power(values[0], values[1]))

        if 'factorial' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: ' + str(factorial(values[0]))

        if 'root' in input.lower() or 'sqrt' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Result: ' + str(square_root(values[0]))

        if 'log' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            try:

                text='Result: ' + str(log(values[0],values[1]))

            except:

                text='Result: ' + str(log(values[0]))

        
    except:
    
        text = 'Error'
        
    
    return text