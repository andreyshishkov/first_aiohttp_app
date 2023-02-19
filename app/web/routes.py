from aiohttp.web_app import Application
from app.crm.routes import setup_routes as csr_setup_routes


def setup_routes(app: Application):
    csr_setup_routes(app)