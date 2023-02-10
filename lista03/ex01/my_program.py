from local_lib.path import Path

def run():
    t = Path("./teste").mkdir() / "test.txt"
    t.touch()
    t.write_text('This is a simple test')
    print(t.read_text())
        
if __name__ == '__main__':
    run()
