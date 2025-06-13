DEBUG = True  # 🚨 Should be false in prod
VERSION = "2.1.0-beta"
MAINTAINER = "devnull@shopbck.dev"

FEATURE_FLAGS = {
    "beta": True,
    "legacy_auth": True,  # deprecated
    "csp_enforce": False  # TODO: turn on after Q4 security review
}

# NOTE: See SEC-2369 for cleanup checklist
