# Reddit Submission Scraper

This Python script retrieves Reddit submissions from a specified subreddit within a given date range using the Pushshift API. It's designed to collect links to posts, working around Reddit's time window restrictions by using a sliding time window approach.

## Features

- Fetches submissions from a specified subreddit
- Allows date range specification for data collection
- Uses a sliding time window to bypass API restrictions
- Saves results to a CSV file

## Requirements

- Python 3.x
- `urllib` library (usually comes pre-installed with Python)

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Save the script to a file, e.g., `reddit_scraper.py`.
3. Run the script using Python:

   ```
   python reddit_scraper.py
   ```

4. The script will start collecting post links and save them to a file named `posts.csv` in the same directory.

## Configuration

You can modify the following parameters in the script:

- Start date: `"1/8/2016"`
- End date: `"26/8/2018"`
- Time window size (in seconds): `30*60` (30 minutes)
- Subreddit: `"dataisbeautiful"`

Modify these values in the last line of the script:

```python
saveResults(getSubmissions("1/8/2016", "26/8/2018", 30*60, "dataisbeautiful"))
```

## Functions

1. `getHtml(url)`: Retrieves HTML content from a given URL.
2. `getSubmissions(after, before, windowSize, subreddit)`: Fetches submission links within the specified date range and subreddit.
3. `saveResults(submissionLinks)`: Saves the collected links to a CSV file.

## Output

The script generates a file named `posts.csv` containing the links to the retrieved Reddit posts, one per line.

## Rate Limiting

The script includes a simple rate limiting mechanism, pausing for a short time between requests to avoid overwhelming the API. Adjust the `time.sleep(60/200)` line if you need to modify this behavior.

## Error Handling

The script includes basic error handling for URL errors. If a request fails, it will continue with an empty result for that particular request.

## Disclaimer

This script uses the Pushshift API, which is a third-party service. Be sure to comply with Reddit's and Pushshift's terms of service when using this script. Consider implementing more robust error handling and rate limiting for production use.
