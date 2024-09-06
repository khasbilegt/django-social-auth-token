import nox


@nox.session
@nox.parametrize("django", ["4.2", "5.0", "main"])
def test(session, django):
    if django == "main":
        session.run("pip", "install", "https://github.com/django/django/archive/main.tar.gz")  # noqa E501
    else:
        session.run("pip", "install", f"django=={django}")
    session.run("coverage", "run", "-m", "pytest", "tests")
    session.run("coverage", "report")
    session.run("coverage", "xml")
