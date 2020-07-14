from flask import Flask, request, render_template
from pathlib import Path


app = Flask(__name__)
base_dir = Path.cwd()


@app.route('/', methods=['GET'])
def read_api():
    if request.method == 'GET':
        file_name = request.args.get('file', 'file1').strip().lower()
        file_path = f'{base_dir}/{file_name}.txt'
        error, lines = None, None
        try:
            encoding = 'utf-16' if file_name in ['file2', 'file4'] else 'utf-8'
            with open(file_path, 'r', encoding=encoding) as f:
                lines = f.readlines()
                start = int(request.args.get('start', 1))
                end = int(request.args.get('end', len(lines)))
                lines = lines[start-1:end]
                if file_name != 'file4':
                    lines = [line.split(':') for line in lines]
                    lines = [line[1].strip() for line in lines if len(line) > 1]
        except FileNotFoundError:
            error = 'File not found!!'
        except KeyError:
            error = 'Please check the URL!!'
        except Exception:
            error = 'Internal Server Error!!'
        return render_template('index.html', lines=lines,
                               title=file_name.title(),
                               error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
