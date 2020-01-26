# ASS Karaoke Tag Cloner
## About
* This small Python script can greatly reduce your effort in timing karaoke syllable-by-syllable in Aegisub.
* The idea of this script bases off the fact that the difference in karaoke timing between verse 1 and verse 2 of a song is not considerable. This script will extract the karaoke tags from your "source" lines and paste them over your "destination" lines.
* After using this script, you can paste the result lines back into Aegisub and make some other small adjustments if needed. Much more time-saving than re-timing verse 2 of your song syllable-by-syllable again, and totally from scratch.

## Files needed
* Python 3.x have to be installed.

The root folder of this script should contain these files:
* **input_src.txt**: contains the lines that you want to copy karaoke tags from.
* **input_dest.txt**: contains the lines that you want to paste your tags over.

    I will further explain how to use these files in the next section.
    You can also open the example files come along with the script to understand more.
## How to use

### Warning
* **input_src.txt** and **input_dest.txt** must has the same number of lines.
* Each line of **src** and **dest** MUST has the same number of syllables.

    If your input data violates one of the above, the program will halt and you will be prompted to correct your mistakes.
* Styling tags in **input_src.txt** at the beginning of each line must be removed. The program provides you with an option to do this.

    For example, **{\fade(100,100)\blur5}** should be removed.
    ```
    ... {\fade(100,100)\blur5} {\k21} Fu{\k27}da{\k20}n {\k24}yo{\k23}ri...
    ```
* Besides karaoke tags (e.g. *{\k21}*), your input lines **must not** contain any acute brackets ```{ }```. Otherwise the program will not work correctly.

### Steps
1. Open Aegisub and copy the lines that you want to use as your karaoke tag "source". Paste them in **input_src.txt**.
2. Copy the lines that you want to paste the tags over. Paste them in **input_dest.txt**.
3. Mark your syllables in **input_dest.txt** with the pipeline character ```|```. You have to mark the beginning of your lyric with a pipeline character as well. There is no need to replace the spaces in the line with pipeline characters. Your newly marked syllables should match what you previously marked in your **input_src.txt**. Pay attention to the number of syllables.

    For example (from *Mogyutto "Love" de Sekkin-chuu*):
    ```
    Dialogue: 0,0:02:23.17,0:02:29.67,Up,,0,0,0,, |Na|ni|ka chi|gau do|ki do|ki da|re wo sa|sou shi|ri|ta|i
    ```
4. Run the script named **program.py**.
5. Enter **ALL** of the styling tags that you use at the beginning of each line **exactly** if any, without the acute brackets. Type **none** if there is no styling tag.

    For example, you should enter ```\fade(100,100)\blur5``` if your input looks like this.
    ```
    ... {\fade(100,100)\blur5} {\k21} Fu{\k27}da{\k20}n {\k24}yo{\k23}ri...
    ```
6. Correct your mistakes if you are prompted.
7. A file named **result.txt** will be generated in the same folder if the process successes. Open it and copy all its lines (press **Ctrl-A**, then **Ctrl-C** on your keyboard).
8. Return to Aegisub. Right-click on the first line in your previously selected lines. Click on **Paste over...**.
9. Tick the box next to **Text**. Scroll down if you cannot find it.
10. Adjust the difference in timing in verse 2.
