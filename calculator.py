def add(x, y):
    return x + y

def subtract(x, y):  
    return x - y

def multiply(x, y):
    return x * y

def calculator(x, y, operator):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply
    }

    if operator in operations:
        return operations[operator](x, y)
    else:
        return "Invalid operator"

def lambda_handler(event, context):
    try:
        x = float(event['x'])
        y = float(event['y'])
        operator = event['operator']
        result = calculator(x, y, operator)
        return {
            'statusCode': 200,
            'body': {
                'result': result
            }
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': f'Missing parameter: {str(e)}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

if __name__ == "__main__":
    x = 5
    y = 4
    operator = '-'
    result = calculator(x, y, operator)
    print("Result: ", result)
