# Use the official Python image as a base image
FROM python:3.8

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install the required packages
RUN apt-get update -y && \
    apt-get install -y \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgcc1 \
    libgconf-2-4 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and Streamlit app to the container
COPY requirements.txt /app/requirements.txt
COPY your_streamlit_app.py /app/your_streamlit_app.py

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port for Streamlit
EXPOSE 8501

# Set the command to run your Streamlit app
CMD ["streamlit", "run", "ty.py"]
