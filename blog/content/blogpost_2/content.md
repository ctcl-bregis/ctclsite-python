I rewrote the website in Python... again

## Why I switched back to Python
Starting sometime in November 2022, I decided to rewrite the website code in Rust with the idea that it would fix the processing time for RAMList lists that were greatly increasing in size.

I rewrote the website again in Python mostly because I am still a complete beginner to the Rust programming language so I was concerned if I tried to update any content or code I might end up breaking something then would not know how to fix it.

### Performance Fix
Before I rewrote the website in Rust, the code for loading RAMList list content was very inefficient. On *every page load* all of the CSV files for the requested list page were loaded then rendered. 

Now, all of the list content files (CSV) are accessed once on Flask webserver startup and put into a single dictionary of dictionaries for each list type (ddr4, mobile, etc.). Not having to load every CSV file from disk on each request significantly improves load times, CPU usage and disk usage.

As of the first release of this rewrite; version 3.1.0, the load times for RAMList lists are not really noticibly different from when the website used Rust.


