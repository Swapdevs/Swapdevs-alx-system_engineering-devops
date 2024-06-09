#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        # Check if the subreddit exists (404 error)
        if response.status_code == 404:
            print(None)
            return

        # Parse the response as JSON and check for valid data
            results = response.json().get("data")
            if results is None or "children" not in results:
                print(None)
                return
            
            # Print the titles of the posts
            for post in results.get("children", []):
                print(post.get("data", {}).get("title"))
        
        # Handle JSON decode error
        except ValueError:
            print(None)

    # Handle other potential network errors
    except requests.RequestException:
        print(None)
