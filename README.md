# Less We Correct

A Twitter bot that corrects people who say "less we forget" instead of "lest we forget".

To run, use the command:
```
nohup python lesswecorrect.py > lesswecorrect.log &
```

If you are running it on a remote host, you can use screen and then disconnect your session.
```
screen -R LessWeCorrect
nohup python lesswecorrect.py > lesswecorrect.log &
```

Then close the screen
```
ctrl+a
d
```