# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="recursos\cachorro.ico") ]
cx_Freeze.setup(
    name = "Scooby",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["recursos"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi
