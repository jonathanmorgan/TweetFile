# TweetFile README
## parsing notes

- Item name starts at beginning of a new line.
- Tab between field name and field value.
- Two blank lines between tweets
- Does not break out at-mentions - might need to make that a parsing pass.

## Fields:
- ID
- User
- UserID
- Text - can be multiple lines - Does Time always follow text?
- Time
- Language
- Coordinates (optional) - lat, long
- UserLocation
- RetweetID (optional)
- RetweetUser (optional)
- URL (optional) - if multiple URLs, multiple URL lines with one URL per URL line.
- HT (optional) - if multiple hash tags, will have multiple HT lines, with one hash tag per HT line.

## Notes on parsing:
- base end of text on pulling in lines until you reach another known field.
- need capacity to store un-knowns (beginning of line doesn't fit any defined field type).
- want to get at-mentions, eventually.
- all languages, so need to make sure we are supporting unicode.

## Questions:
- how to store URLs, hashtags?  To start, just a list in a text field...?

## Todo:
- in that application, in models, create TweetFile model that just stores file name, date of file (start and end date?), update and create dates, path to exported SQL for file...

### in TweetNet:
- make relation from Tweet to Twitter_User model optional, add fields to store raw IDs, so we can create, tie things together later.  Perhaps this is a separate package?
- abstract out tweet, tweet user from ideology stuff - make abstract tweet and tweet_user in separate twitter package (include there also a concrete class for tweet, tweet user).  Then in tweet net, extend tweet, tweet_user, add in ideology stuff.

### in TweetFile:
- method that accepts a file system path to a tweet file, date of file, and optional end date (for date range), then opens that file and parses it line-by-line, two full blank lines between tweets, don't enforce order of fields except for Text and Time - Use Time to figure out when Text ends.  Because of python file handling, also make sure to strip newline off the end of each line except for within Text.  For now, place information in database, don't resolve URLs.
- method to resolve URLs that can be run while files are being parsed.
- method to parse @-mentions from tweets that can be run while files are being parsed.
- could resolve URLs and @-mentions during processing.  We'll see how it handles this size of file.
- If memory is limiting, then look up django garbage collection, implement garbage collection in file processing.