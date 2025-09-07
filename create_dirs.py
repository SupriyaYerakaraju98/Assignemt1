import os

for i in range(1, 4):
    dir_name = str(i)
    os.makedirs(dir_name, exist_ok=True)

        for j in range(1, i + 1):
        file_path = os.path.join(dir_name, f"{j}.txt")
        with open(file_path, "w") as f:
            f.write(f"This is file {j}.txt in the directory {dir_name}\n")