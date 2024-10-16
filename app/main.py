from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="public/views")

@app.get("/thiep-moi", response_class=HTMLResponse)
async def thiep_moi(request: Request):
    # Access the "guest" query parameter
    guest = request.query_params.get("g", "Khách mời")
    if "_" in guest:
        guest = guest.replace("_", " ") 
    print(f"Guest name: {guest}")

    # Render the HTML file with the guest name
    return templates.TemplateResponse("index.html", {"request": request, "guest": guest})

@app.get("/", response_class=HTMLResponse)
async def thiep_moi_2(request: Request):
    # Access the "guest" query parameter
    guest = request.query_params.get("g", "Khách mời")
    if "_" in guest:
        guest = guest.replace("_", " ") 
    print(f"Guest name: {guest}")

    # Render the HTML file with the guest name
    return templates.TemplateResponse("index-me.html", {"request": request, "guest": guest})