from threading import Thread
from pathlib import Path

def search_keywords_in_files_threading(files, keywords, results):
    for file in files:
        found = []
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                found = [word for word in keywords if word in content]
        except Exception as e:
            print(f"Error reading {file}: {e}")
        results.append((file, found))

def threading_search(files, keywords):
    num_threads = 4
    chunk_size = len(files) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        chunk = files[i * chunk_size: (i + 1) * chunk_size]
        thread = Thread(target=search_keywords_in_files_threading, args=(chunk, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for file, found in results:
        print(f"File: {file}, Keywords found: {found}")


if __name__ == "__main__":
    files = ["textfile_1.txt", "textfile_2.txt", "textfile_3.txt", "textfile_4.txt"]
    keywords = ["error", "warning", "critical"]
    threading_search(files, keywords)

