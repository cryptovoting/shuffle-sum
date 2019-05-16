# Shuffle-Sum

Tallying of single transferable vote ballots using the [Shuffle-Sum](https://talmoran.net/papers/BMNRT09-shuffle-sum.pdf?fbclid=IwAR0jZ18H2ZYMsCjPkW-3ohDNom5UjbK-jMen6_lISVoWJJnPWM0A41KAS1Y) protocol.

## Installation

Requires Python 3.6+.

```bash
git clone https://github.com/cryptovoting/shuffle-sum.git
cd shuffle-sum
pip install -e .
```
*Note that the `-e` flag will instruct pip to install the package as "editable". That is, when changes are made to any part of the package during development, those changes will immediately be available system-wide on the activated python environment.*

All requirements for this package should be added to `setup.py`.

## Real Election Data

San Francisco voting data from the November 2016 Board of Supervisors election was downloaded from the [Ranked Choice Voting Resource Center](https://www.rankedchoicevoting.org/data_clearinghouse) and is available in the `data` directory. The script for converting the San Francisco ballot image data to our CandidateOrderBallot format is in `scripts/load_ballot_data.py`. It can be run with:

```bash
python scripts/load_ballot_data.py --master_lookup data/san_francisco_nov_2016_master_lookup.txt --ballot_image data/san_francisco_nov_2016_ballot_image.txt
```
