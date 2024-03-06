from waitress import serve
from hmt_project.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000')