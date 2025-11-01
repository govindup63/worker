FROM python:3.11-slim

WORKDIR /app
# Install required packages
RUN pip install --no-cache-dir fastmcp>=2.0.0 uvicorn starlette
# Copy application code
COPY . .
# Expose port
EXPOSE 8080
# Set environment variables
ENV MCP_TRANSPORT=sse
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8080
# Run the server
CMD ["python","server.py"]