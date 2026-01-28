FROM nginx:alpine

# Copy index.html and health.html
COPY index.html /usr/share/nginx/html/index.html
COPY health.html /usr/share/nginx/html/health

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
