# data-science-api

This API allows for various operations on datasets, primarily focusing on manipulating and analyzing Excel files. The goal is to provide a simple interface to interact with different datasets, enabling operations such as sampling, obtaining unique values, grouping, and extracting quantiles.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <directory-name>
   ```

2. Build the image
   ```bash
   docker build -t dev-data-science-api -f Dockerfile.dev .
   ```
3. Run the container
   ```bash
   chmod +x run.sh # needed the first time
   ./run.sh
   ```

### Push container to heroku

```bash
heroku container:login
heroku create --region eu app_name
heroku stack:set container -a  app_name
heroku container:push web -a app_name
heroku container:release web -a app_name
```

## API Routes

You can read the API documentation on your `url/docs`.

Example :

http://127.0.0.1:4000/docs

## Usage

Once the application is running, you can send requests to the specified routes to perform various data operations.
