import ctypes
lib = ctypes.cdll.LoadLibrary('./libtest.dll')
print(lib.test(1))