#!/bin/bash
uvicorn apps.serving.app.main:app --reload
