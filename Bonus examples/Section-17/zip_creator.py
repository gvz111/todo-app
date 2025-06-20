import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path=pathlib.Path(dest_dir,"file.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["bonus16.py","empty.py"],dest_dir=r"C:\Users\Armsapphire\Desktop\Udemy\Bonus examples\Section-17")
                        