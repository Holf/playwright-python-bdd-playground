# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.29.0-focal

# Add python script to Docker
COPY . .

RUN pip install -r requirements.txt

# Run Python script
CMD [ "python3", "-m", "pytest", "tests" ]