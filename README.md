# NBA Lineup Tracker

This Python script allows you to track and analyze NBA team lineups based on data from the website "popcornmachine.net". You can input a specific NBA team using its three-letter code and choose how many games you'd like to track. The script then retrieves lineup data from the website, processes it, and provides various options for displaying and analyzing the collected data.

***This program is currently limited due to the offseason, it can only find games played after the second round of the playoffs. It will return to normal functionality after the first games of the regular season. To learn more, see the Note at the end of the ReadME***

## Prerequisites

To run this script, you'll need:

- Python installed on your system.
- The `requests` library for making HTTP requests.
- The `BeautifulSoup` library for parsing HTML content.

You can install the required libraries using the following commands:

```bash
pip install requests
pip install beautifulsoup4
```

## How to Use

1. Open a terminal and navigate to the directory containing the `lineupTracker.py` script.

2. Make the script executable if necessary. Run the following command:

   ```bash
   chmod +x lineupTracker.py
   ```

3. Run the script using the command:

   ```bash
   ./lineupTracker.py
   ```

4. Follow the prompts to input the desired NBA team (using the three-letter code) and the number of games to track.

5. The script will fetch lineup data from "popcornmachine.net," process it, and present you with various options:

   - Print all lineups.
   - Print the five best and five worst lineups.
   - Find lineups containing specific players.
   - Remove lineups containing specific players.

6. Select an option by entering the corresponding number.

## Features

- Retrieves lineup data for a specified NBA team from multiple games.
- Calculates total playing time for each lineup.
- Offers options to display and analyze lineup data based on user preferences.

## Note

Please be aware that the script fetches data from an external website, and its functionality might be affected if the website's structure or data format changes. The script may need adjustments in such cases.
The program is currently limited to games since the Western Conference Finals, so it is currently limited.

## Disclaimer

This script is provided as-is and may not have full error handling or extensive testing. Use it responsibly and feel free to modify it to suit your needs.

For more information about the script's implementation and functions, refer to the script's comments and the [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

**Author**: Leo Chao

**Date**: 2023/08/13
