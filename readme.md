Assesment Level 1
=================

Ilian's Fedora update went good. However he needs a detailed info about his latest Qt libraries upgrade. He provides you with his `dnfhistory.txt` file in the `Data` repo.

Your tasks:
==========
- Using `Command.py` module, you are about to `git pull` the `dnfhistory.txt`. 
- Using your knowledge of `string` and `files` you are about to read the file line by line and parse each line.
- Using your knowledge you have to find all lines containing `qt5`.
- You have to create a helper `class` that will hold that information using a minimal `facade pattern`.
- You have to aggregate all meaningful information into the class.
- For more kudos, you have to omit `qscintilla` and `python` in lines with `qt`
- You have to write all data from the class in a `txt` file in a format as: `qt5-qtquickcontrols installed at  2019-12-10 15:15`
- Finally, our `Command` class has to call `git add yourfile.txt`, `git commit -m 'db update' ` and `git push` to the `Data` repo.

Time limit (1 week)
Optimal time (1 day)

Enjoy
