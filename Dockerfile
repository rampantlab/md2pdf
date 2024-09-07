# Use a base image with minimal TeX Live and Python installed
FROM python:3.9-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/usr/local/texlive/2024/bin/x86_64-linux:$PATH
ENV TEXMFHOME=/root/texmf

# Install necessary utilities and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    perl \
    make \
    ghostscript \
    ca-certificates \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Pygments for minted package support
RUN pip install Pygments

# Download and install TeX Live with 'scheme-basic' (minimal installation)
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar -xzf install-tl-unx.tar.gz && \
    cd install-tl-* && \
    ./install-tl --scheme=basic --no-interaction

# Initialize tlmgr in user mode
RUN tlmgr init-usertree

# Force update tlmgr repositories to ensure latest metadata
RUN tlmgr update --self && tlmgr update --all

# Install necessary LaTeX packages via tlmgr
RUN tlmgr install \
    fontspec \
    xcolor \
    enumitem \
    framed \
    markdown \
    paralist \
    parskip \
    etoolbox \
    listings \
    csvsimple \
    pgf \
    fancyvrb \
    gobble \
    verse \
    soul \
    minted

# Set the working directory
WORKDIR /app

# Copy Files into the container
COPY md2pdf.py /app
COPY templates/* /app

# Run the python script when the container starts (but let users pass arguments)
ENTRYPOINT ["python3", "md2pdf.py"]
