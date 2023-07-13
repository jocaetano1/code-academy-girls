from flask import Flask, render_template, request, redirect

from use_cases.register_student import RegisterStudent
from use_cases.list_student import ListStudent
from adaptors.inmem.inmem_student_repository import InmemStudentRepository

app = Flask(__name__)


@app.get("/students")
def list_student_view():
    repository = InmemStudentRepository()
    list_student = ListStudent(repository)
    students = list_student.execute()
    return {"status_code": "200", "students": students}


@app.route("/students/create", methods=["GET", "POST"])
def register_student_view():
    if request.method == "POST":
        data = request.form
        repository = InmemStudentRepository()
        register_student = RegisterStudent(repository)
        register_student.execute(data)
        return redirect("/students")
    return render_template("register_student.html")


if __name__ == "__main__":
    app.run("localhost", 8001)
