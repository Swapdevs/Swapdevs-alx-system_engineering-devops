# Reddit API Subscriber Count

This project contains a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

## Files

- `0-subs.py`: Contains the `number_of_subscribers` function.
- `0-main.py`: Script to test the function.
- `README.md`: Project documentation.

## Function Details

### `number_of_subscribers`

Queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, returns 0.

#### Arguments

- `subreddit` (str): The name of the subreddit to query.

#### Returns

- `int`: Number of subscribers or 0 if subreddit is invalid.

## Usage

Run `0-main.py` with the name of the subreddit as an argument.

Example:

```sh
python3 0-main.py programming
