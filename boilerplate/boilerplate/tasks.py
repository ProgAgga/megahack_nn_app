from boilerplate.celery import app


@app.task()
def scan_orders():
    pass
