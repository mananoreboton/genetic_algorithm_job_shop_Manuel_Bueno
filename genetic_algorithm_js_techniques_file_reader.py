import genetic_algorithm_js_techniques_evaluator as ev

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
            ev.evaluate_techniques(file_content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")