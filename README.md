# NameMC Player Scraper
Small Python script which scrapes player names and unique ids, by using their Friends API.

## How to use:
Download the Python file and run it using:

`python player_scraper.py`

The program will ask you for an UUID which will assume is a player with friends.

Beware this script won't work if you put one that doesn't!

## Results:
Once you stop the program, all queries will be saved in the file "players.txt" with the format:

```text
user,unique id
```

Example:
 
```text
Acucanu,e7a9f4d6-2c5f-4971-aa57-3db8cfe99575
aestqetic,91135673-1403-4695-8a8b-ee684a9d89df
etc... etc...
```
