import os
import shutil
from app import app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(BASE_DIR, 'build')


def ensure_build_dir():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR, exist_ok=True)


def write_nojekyll():
    open(os.path.join(BUILD_DIR, '.nojekyll'), 'w').close()


def copy_static():
    src = os.path.join(BASE_DIR, 'static')
    dst = os.path.join(BUILD_DIR, 'static')
    if os.path.exists(src):
        shutil.copytree(src, dst)


def render_routes():
    client = app.test_client()
    routes = ['/', '/saved']
    for route in routes:
        resp = client.get(route)
        if resp.status_code == 200:
            filename = 'index.html' if route == '/' else route.strip('/').replace('/', '_') + '.html'
            path = os.path.join(BUILD_DIR, filename)
            with open(path, 'wb') as f:
                f.write(resp.get_data())
            print(f'Wrote {path}')
        else:
            print(f'Skipped {route}: status {resp.status_code}')


def main():
    ensure_build_dir()
    copy_static()
    render_routes()
    write_nojekyll()
    # Also write a site-level index.html at the repository root for GitHub Pages
    built_index = os.path.join(BUILD_DIR, 'index.html')
    if os.path.exists(built_index):
        shutil.copyfile(built_index, os.path.join(BASE_DIR, 'index.html'))
        print('Wrote index.html to repository root')
    print('Build complete. Output in build/')


if __name__ == '__main__':
    main()
