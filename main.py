
__author__ = 'DrJonoG'  # Jonathon Gibbs

#
# Copyright 2016-2020 https://www.jonathongibbs.com / @DrJonoG
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and limitations under the License.
#

import os
import sys
import pandas as pd
import argparse
import yahoo

def main(destinationPath, symbolPath):
    # Select first column as symbiol name
    symbolList = pd.read_csv(symbolPath).iloc[:, 0]

    # Ensure folders exist
    if destinationPath:
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)

    # Iterate through each of the tickers and download data
    for index, sym in symbolList.items():
        symDF = yahoo.Download(symbol=sym, dataRange='60d', dataInterval='5m')


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', required=True, help='Download destination')
    parser.add_argument('-s', required=True, help='Path to symbol list (csv)')
    args = parser.parse_args()
    # Call
    main(args.d, args.s)
