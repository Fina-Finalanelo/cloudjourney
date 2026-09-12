Docker Portfolio Container

Containerised portfolio website using nginx and Docker.

How to build:
docker build -t fina-portfolio .

How to run:
docker run -d -p 8080:80 --name my-portfolio fina-portfolio

Then visit: http://localhost:8080

How to stop:
docker stop my-portfolio
docker rm my-portfolio

What the Dockerfile does:
- Starts from official nginx:alpine base image (5MB)
- Copies portfolio page into nginx web root
- Exposes port 80
- Starts nginx when container runs

Why Docker?
- Runs identically everywhere - laptop, EC2, anywhere
- No dependency conflicts
- Lightweight and fast
- Industry standard for application deployment
