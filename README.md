# SimpleOTXScript
To Use:
  1. Make sure you have Python and pip installed 
  2. Install OTXv2 either by:
    a. using pip
      'python -m pip install OTXv2' 
    b. or cloning the repo at https://github.com/AlienVault-OTX/OTX-Python-SDK and "python pip install ."
    c. Or following the instructions from the above link 
  3. Clone this repo or just copy the script and save in your own file
  4. In the script, change the keys in the otxlist to the keys of the pulses you want to scrape.
     * you can find it by copying the 24 character string in the link 
  4. Run using "python otxprint.py"
  5. To pipe into a text file, use ">"
    e.g. 'python otxprint > "test.txt" '
