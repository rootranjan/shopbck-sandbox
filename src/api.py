# TODO: Replace with actual API handler
# FIXME: Request validation missing in this mockup

def handle_request(request):
    # Simulated legacy endpoint
    user_agent = request.get("headers", {}).get("User-Agent", "unknown")
    return {
        "status": "ok",
        "user": request.get("user", "guest"),
        "agent": user_agent,
        "debug": False  # force disable debug in prod
    }
