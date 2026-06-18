---

## 📄 organizer.py
```python
import os
import shutil

def organize_folder(path):
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue

        extension = file.split(".")[-1].lower()

        if extension in ["jpg", "png", "jpeg"]:
            folder = "Images"
        elif extension in ["mp4", "mkv", "mov"]:
            folder = "Videos"
        elif extension in ["pdf", "docx", "txt"]:
            folder = "Documents"
        else:
            folder = "Others"

        folder_path = os.path.join(path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(file_path, os.path.join(folder_path, file))

    print("Arquivos organizados com sucesso!")


if __name__ == "__main__":
    current_folder = os.getcwd()
    organize_folder(current_folder)