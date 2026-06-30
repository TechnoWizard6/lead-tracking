from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from database import (
    get_db,
    get_lead_by_token,
    log_activity
)
from whatsapp import send_whatsapp
from datetime import datetime
import traceback
import os

app = FastAPI(
    title="Lead Tracking API",
    version="1.0.0"
)

DEFAULT_REDIRECT = "https://6a3d17e4f455624e2c44955a--relaxed-buttercream-4fb006.netlify.app"


@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Lead Tracking API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.utcnow().isoformat()
    }


@app.get("/page/{lead_token}")
def track_page(lead_token: str, request: Request):

    try:

        db = get_db()

        lead = get_lead_by_token(db, lead_token)

        if lead is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Lead not found"
                }
            )

        ip_address = request.client.host

        log_activity(
            db=db,
            lead_token=lead_token,
            event="page_open",
            activity="Lead opened the page",
            ip_address=ip_address
        )

        message = f"""
🔔 Live Activity Alert!

Lead Name: {lead["name"]}

Phone: {lead["phone"]}

Event: page_open

Activity:
Lead opened the page

Page:
{lead["page_name"]}

URL:
{lead["page_url"]}

Time:
{datetime.utcnow().isoformat()}Z
"""

        send_whatsapp(message)

        redirect_url = lead["page_url"]

        if redirect_url is None:
            redirect_url = DEFAULT_REDIRECT

        return RedirectResponse(
            url=redirect_url,
            status_code=302
        )

    except Exception as e:

        traceback.print_exc()

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
