# How to build a custom python
1. Download a copy of CPython source code
```
$ git clone https://github.com/python/cpython
$ cd cpython
```
2. Checkout a version. Take version 3.9.0 for example
```
$ git checkout tags/v3.9.0 -b v3.9.0
```
for macOS  
3. Install the C compiler and toolkit
```
xcode-select --install
```
4. If no Homebrew is installed, install it.
```
$ /usr/bin/ruby -e "$(curl -fsSL \
 https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
5. Install the dependencies for cpython
```
$ brew install openssl xz zlib gdbm sqlite
```
