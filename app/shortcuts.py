from pathlib import Path

from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / 'templates'
templates = Jinja2Templates(str(TEMPLATES_DIR))

def render(template_name: str, context: dict):
    return templates.TemplateResponse(template_name, context)


