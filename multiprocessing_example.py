import multiprocessing
from pathlib import Path

def search_keywords_in_files_multiprocessing(files, keywords, queue):
    for file in files:
        found = []
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                found = [word for word in keywords if word in content]
        except Exception as e:
            print(f"Error reading {file}: {e}")
        queue.put((file, found))

def multiprocessing_search(files, keywords):
    num_processes = 4
    chunk_size = len(files) // num_processes
    processes = []
    queue = multiprocessing.Queue()

    for i in range(num_processes):
        chunk = files[i * chunk_size: (i + 1) * chunk_size]
        process = multiprocessing.Process(target=search_keywords_in_files_multiprocessing, args=(chunk, keywords, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        file, found = queue.get()
        print(f"File: {file}, Keywords found: {found}")


if __name__ == "__main__":
    files = ["textfile_1.txt", "textfile_2.txt", "textfile_3.txt", "textfile_4.txt"]
    keywords = ["error", "warning", "critical"]
    multiprocessing_search(files, keywords)

