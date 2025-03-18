# Using Node.js image as base
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the entire frontend code
COPY . .

# Build the React app
RUN npm run build

# Serve the app with a lightweight server
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3050"]

# Expose port 3050
EXPOSE 3050