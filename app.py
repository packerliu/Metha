#from flask import Flask, request

#app = Flask(__name__)

# Your existing argparse code
import argparse

#@app.route('/', methods=['GET'])
    
def index():
    args = parser.parse_args()
    name = request.args.get('name', args.name)
    age = request.args.get('age', args.age)

    return f'Hello, {name}! You are {age} years old.'

def welcome(opts):
    print("Hello {name},\nthis is a simple example.".format(name=opts.name))

def main():
    """
    Parse command-line arguments and then call the corresponding functions
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--age', type=int, default=18)

    
    # Now we use argparseweb instead of original command above
    args = parser.parse_args()
    #args = webui.Webui(parser).getone()
    print("Hello {name} at age {age}, this is a simple example.". \
          format(name=args.name, age=args.age))
    
    #webui.Webui(parser).dispatch(welcome, parsed=True)

    

if __name__ == '__main__':
    main()
    #app.run(debug=True)
