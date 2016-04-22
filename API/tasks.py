import os

from backend.celery import app

from API.models import BlockVizRequest

@app.task(bind=True)
def generate_block_viz(self, id):
	print("Reached")