import argparse


def app():
    parser = argparse.ArgumentParser(description="A simple CLI tool.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    
    print('hello world')
    
    return 0