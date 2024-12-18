from setuptools import setup, Extension

def main():
    setup(name="hello",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("hello", ["hello.c"])])

if __name__ == "__main__":
    main()