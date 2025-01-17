import os
import argparse
import job_shop_techniques_evaluator
from job_shop_data import JobShopData

def read_single_txt_file(file_path: str):
    if not file_path.endswith('.txt'):
        print(f"The specified file is not a .txt file: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            if file_content == 0:
                print(f"The specified file is empty: {file_path}")
                return
            job_shop_data = JobShopData(text=file_content)
            job_shop_data.show_jobs()
            job_shop_techniques_evaluator.evaluate_techniques(job_shop_data=job_shop_data)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")

def read_txt_files(directory: str):
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
        if not files:
            print(f"No .txt files found in the directory: {directory}")
            return

        for file in files:
            read_single_txt_file(file)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except Exception as e:
        print(f"Error reading files from the directory {directory}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Reads Job Shop test cases from .txt files in a directory.")
    parser.add_argument("-d", "--directory", type=str, help="Directory to read .txt files from.")
    parser.add_argument("-f", "--file", type=str, help="Specific .txt file to read.")
    args = parser.parse_args()

    if args.directory:
        read_txt_files(args.directory)
    elif args.file:
        read_single_txt_file(args.file)
    else:
        current_directory = os.getcwd()
        print(f"Reading .txt files from the current directory: {current_directory}")
        read_txt_files(current_directory)

if __name__ == "__main__":
    main()
