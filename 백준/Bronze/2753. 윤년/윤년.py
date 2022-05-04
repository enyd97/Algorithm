N = int(input())
print(1 if ((N % 4 == 0) & (N % 100 != 0)) | (N % 400 == 0) else 0)